%global tl_name beuron
%global tl_revision 46374
%global tl_version 1.3

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The script of the Beuronese art school
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/beuron
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the script used in the works of the Beuron art
school for use with TeX and LaTeX. It is a monumental script consisting
of capital letters only. The fonts are provided as Metafont sources, in
the Type1 and in the OpenType format. The package includes suitable font
selection commands for use with LaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from beuron:
Map beuron.map
TL_DROPIN_EOF
