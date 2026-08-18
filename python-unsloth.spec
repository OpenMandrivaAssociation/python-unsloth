Name:		python-unsloth
Version:	2026.8.18
Release:	1
Summary:	Faster LoRA / QLoRA / RL fine-tuning for LLMs
License:	Apache-2.0 AND AGPL-3.0-only
Group:		Development/Python
URL:		https://github.com/unslothai/unsloth
Source0:	https://files.pythonhosted.org/packages/source/u/unsloth/unsloth-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	python%{pyver}dist(unsloth-zoo)
Requires:	python%{pyver}dist(torch)
Requires:	python%{pyver}dist(transformers)
Requires:	python%{pyver}dist(peft)
Requires:	python%{pyver}dist(accelerate)
Requires:	python%{pyver}dist(huggingface-hub)
Requires:	python%{pyver}dist(diffusers)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(packaging)
Requires:	python%{pyver}dist(tqdm)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(protobuf)
Requires:	python%{pyver}dist(pydantic)
Requires:	python%{pyver}dist(pyyaml)
Requires:	python%{pyver}dist(click)
Requires:	python%{pyver}dist(rich)
Requires:	python%{pyver}dist(typer)
Requires:	python%{pyver}dist(tyro)
Requires:	python%{pyver}dist(structlog)
Requires:	python%{pyver}dist(nest-asyncio)
Requires:	python%{pyver}dist(hf-transfer)
Requires:	python%{pyver}dist(torchvision)
Requires:	python%{pyver}dist(datasets)
Requires:	python%{pyver}dist(trl)
Requires:	python%{pyver}dist(sentencepiece)
Recommends:	python%{pyver}dist(bitsandbytes)
Recommends:	python%{pyver}dist(triton)
Recommends:	python%{pyver}dist(xformers)

# Do not let the generator emit NVIDIA-only extras as hard Requires.
%global __requires_exclude ^python[0-9.]+dist\\((bitsandbytes|triton|xformers)\\)

%description
Unsloth patches Hugging Face Transformers / PEFT for faster LoRA and
QLoRA fine-tuning. Works with the system python-torch (including the
ROCm build). Export a trained adapter with PEFT, convert it with
llama.cpp convert_lora_to_gguf.py, then merge with llama-export-lora
or load it at runtime via llama-cli --lora.

  unsloth --help

NVIDIA-only extras (bitsandbytes, xformers, triton) are recommended
when present, not required.

# Accept cooker torch 2.13 / transformers 5.15 / current datasets+trl.
# Drop NVIDIA-only hard deps so the auto-requires generator cannot
# emit uninstallable python3.14dist() pins.
%prep -a
python - <<'PY'
from pathlib import Path
import re
p = Path("pyproject.toml")
t = p.read_text()
t = t.replace('"torch>=2.4.0,<2.12.0"', '"torch>=2.4.0"')
t = t.replace('"datasets>=3.4.1,!=4.0.*,!=4.1.0,<4.4.0"', '"datasets>=3.4.1"')
t = t.replace('"trl>=0.18.2,!=0.19.0,<=0.24.0"', '"trl>=0.18.2"')
t = re.sub(r'"transformers>=4\.51\.3,[^"]+"', '"transformers>=4.51.3"', t)
out = []
for line in t.splitlines(True):
    if any(k in line for k in ("bitsandbytes", "triton>=", "triton-windows", "xformers>=")):
        continue
    out.append(line)
p.write_text("".join(out))
print("patched pyproject.toml")
PY

# pip writes .pyc then touches .py; extra tests treat that as
# python-bytecode-inconsistent-mtime (over the badness cap).
%install -a
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find %{buildroot} -name '*.pyc' -delete

%files
%doc README.md
%license LICENSE
%{_bindir}/unsloth
%{py_sitedir}/unsloth
%{py_sitedir}/unsloth_cli
%{py_sitedir}/studio
%{py_sitedir}/unsloth-*.*-info
