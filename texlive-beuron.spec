%global tl_name beuron
%global tl_revision 46374

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	The script of the Beuronese art school
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/beuron
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the script used in the works of the Beuron art
school for use with TeX and LaTeX. It is a monumental script consisting
of capital letters only. The fonts are provided as Metafont sources, in
the Type1 and in the OpenType format. The package includes suitable font
selection commands for use with LaTeX.

