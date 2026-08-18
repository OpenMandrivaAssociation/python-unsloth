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
# Optional NVIDIA-centric stack — not needed for PEFT LoRA on ROCm.
Recommends:	python%{pyver}dist(sentencepiece)
Recommends:	python%{pyver}dist(datasets)
Recommends:	python%{pyver}dist(trl)
Recommends:	python%{pyver}dist(bitsandbytes)
Recommends:	python%{pyver}dist(triton)
Recommends:	python%{pyver}dist(xformers)
Recommends:	python%{pyver}dist(torchvision)

%description
Unsloth patches Hugging Face Transformers / PEFT for faster LoRA and
QLoRA fine-tuning. Works with the system python-torch (including the
ROCm build). Export a trained adapter with PEFT, convert it with
llama.cpp convert_lora_to_gguf.py, then merge with llama-export-lora
or load it at runtime via llama-cli --lora.

  unsloth --help

NVIDIA-only extras (bitsandbytes, xformers, triton) are recommended
when present, not required.

%files
%doc README.md
%license LICENSE
%{_bindir}/unsloth
%{py_sitedir}/unsloth
%{py_sitedir}/unsloth_cli
%{py_sitedir}/studio
%{py_sitedir}/unsloth-*.*-info
