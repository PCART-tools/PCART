<p align="center">
  <img src="logo.svg" alt="PCART" width="420">
</p>

<p align="center">
  Automated Repair of Python API Parameter Compatibility Issues
</p>

<p align="center">
  <a href="https://github.com/PCART-tools/PCART/wiki">Documentation</a> ·
  <a href="https://github.com/PCART-tools/PCART/wiki/Configuration-Guide">Configuration Guide</a> ·
  <a href="https://github.com/PCART-tools/PCART/wiki/How-It-Works">How It Works</a> ·
  <a href="https://github.com/PCART-tools/PCART/wiki/Examples">Examples</a> ·
  <a href="https://pcart-tools.github.io/PCART-doxygen/html">API Docs</a> ·
  <a href="https://github.com/PCART-tools/PCBench">PCBench</a>
</p>

<br>

## News

- **2026-07-24** - Released [PCART v1.4](https://github.com/PCART-tools/PCART/releases/tag/v1.4), featuring isolated run workspaces, structured callsite identities, more flexible and safer cross-platform execution of Python scripts, modules, and tools such as `pytest`, and optional experimental PCResolve integration.

- **2026-05-22** - Experimental [PCResolve](https://github.com/PCART-tools/PCResolve) integration: cross-file symbol-tracing replaces single-file string-matching for API call identification. Opt-in via `pcresolve>=1.0.4`; falls back to existing extraction when not installed.

<br>

## What is PCART?

PCART is an automated tool for detecting and repairing Python API parameter compatibility issues caused by library upgrades.

It supports common parameter compatibility changes, including addition, deletion, renaming, reordering, replacement, positional/keyword conversion, and partial type-change analysis. Default-value changes are not currently implemented.

## Quick Start

```bash
python main.py -cfg your_config.json
```

PCART keeps run workspaces in `PCARTRuns/runs/` by default. For repeated runs on large projects, use `--clean-workspace` to prevent excessive disk usage:

```bash
python main.py -cfg your_config.json --clean-workspace
```

Successful workspaces are removed only after reports are exported. Failed workspaces and all outputs under `Report/runs/` are retained.

Each run uses one tool environment and two configured project environments: `currentEnv` and `targetEnv`.

See the [Quick Start](https://github.com/PCART-tools/PCART/wiki/Quick-Start) and [Configuration Guide](https://github.com/PCART-tools/PCART/wiki/Configuration-Guide) for setup details.

## Citation

If PCART supports your research or development work, please cite the following publication:

```bibtex
@article{PCART_TSE2025,
  author={Zhang, Shuai and Xiao, Guanping and Wang, Jun and Lei, Huashan and He, Gangqiang and Liu, Yepang and Zheng, Zheng},
  journal={IEEE Transactions on Software Engineering},
  title={PCART: Automated Repair of Python API Parameter Compatibility Issues},
  year={2026},
  volume={52},
  number={3},
  pages={723-753},
  doi={10.1109/TSE.2025.3646150}
}
```

## License

PCART is licensed under the GNU Affero General Public License v3.0. See [LICENSE](./LICENSE) for details.
