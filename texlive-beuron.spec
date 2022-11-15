Name:		texlive-beuron
Version:	46374
Release:	1
Summary:	The script of the Beuronese art school
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beuron
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beuron.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the script used in the works of the
Beuron art school for use with TeX and LaTeX. It is a
monumental script consisting of capital letters only. The fonts
are provided as Metafont sources, in the Type1 and in the
OpenType format. The package includes suitable font selection
commands for use with LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beuron
%{_texmfdistdir}/fonts/type1/public/beuron
%{_texmfdistdir}/fonts/tfm/public/beuron
%doc %{_texmfdistdir}/fonts/source/public/beuron
%{_texmfdistdir}/fonts/opentype/public/beuron
%{_texmfdistdir}/fonts/map/dvips/beuron
%doc %{_texmfdistdir}/doc/fonts/beuron

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
