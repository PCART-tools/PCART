from flask import Flask, jsonify, request, abort

def create_app():
    app = Flask(__name__)
    # Simulate database
    tasks = [
        {
            'id': 1,
            'title': '学习Flask',
            'description': '学习如何使用Flask创建API',
            'done': False
        },
        {
            'id': 2,
            'title': '学习装饰器',
            'description': '理解Python装饰器的工作原理',
            'done': False
        }
    ]

    # Custom decorator - verify token
    def token_required(f):
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token or token != 'Bearer my-secret-token':
                abort(401, description="invalid authorization token")
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__  
        return wrapper

    # Custom decorator - record log
    def log_request(f):
        def wrapper(*args, **kwargs):
            app.logger.info(f"Receive Request: {request.method} {request.path}")
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper


    # Get all tasks - use multiple decorators
    @app.route('/api/tasks', methods=['GET'])
    @token_required
    @log_request
    def get_tasks():
        return jsonify({'tasks': tasks})

    # Get one task
    @app.route('/api/tasks/<int:task_id>', methods=['GET'])
    @token_required
    def get_task(task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            abort(404, description="Task Not Found")
        return jsonify({'task': task})

    # Create task
    @app.route('/api/tasks', methods=['POST'])
    @token_required
    def create_task():
        if not request.json or 'title' not in request.json:
            abort(400, description="Missing Required Parameters")
        
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201

    # Update Task
    @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
    @token_required
    def update_task(task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            abort(404, description="Task Not Found")
        
        if not request.json:
            abort(400, description="Missing Request")
        
        task['title'] = request.json.get('title', task['title'])
        task['description'] = request.json.get('description', task['description'])
        task['done'] = request.json.get('done', task['done'])
        
        return jsonify({'task': task})

    @app.errorhandler(400)
    @app.errorhandler(401)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def handle_error(error):
        # 定义默认错误消息
        error_messages = {
            400: "Invalid Request",
            401: "Unauthorized",
            404: "Resource Not Found",
            500: "Internal Server Error"
        }
    
        # 如果有自定义描述则使用，否则用默认
        description = getattr(error, 'description', None)
        if not description:
            description = error_messages.get(error.code, str(error))
    
        response = jsonify({
            'error': description,
            'status_code': error.code
        })
        return response, error.code
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
