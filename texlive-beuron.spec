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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the script used in the works of the Beuron art
school for use with TeX and LaTeX. It is a monumental script consisting
of capital letters only. The fonts are provided as Metafont sources, in
the Type1 and in the OpenType format. The package includes suitable font
selection commands for use with LaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/beuron
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/beuron
%dir %{_datadir}/texmf-dist/fonts/map/dvips/beuron
%dir %{_datadir}/texmf-dist/fonts/opentype/public/beuron
%dir %{_datadir}/texmf-dist/fonts/source/public/beuron
%dir %{_datadir}/texmf-dist/fonts/tfm/public/beuron
%dir %{_datadir}/texmf-dist/fonts/type1/public/beuron
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/Literatur.bib
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/README
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/beuron-de.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/beuron-de.tex
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/beuron-en.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/beuron/beuron-en.tex
%{_datadir}/texmf-dist/fonts/map/dvips/beuron/beuron.map
%{_datadir}/texmf-dist/fonts/opentype/public/beuron/Beuron-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/beuron/BeuronCondensed-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/beuron/BeuronExtended-Regular.otf
%doc %{_datadir}/texmf-dist/fonts/source/public/beuron/beuron.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/beuron/beuronbuchst.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/beuron/beuronc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/beuron/beuronkern.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/beuron/beuronx.mf
%{_datadir}/texmf-dist/fonts/tfm/public/beuron/beuron.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/beuron/beuronc.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/beuron/beuronx.tfm
%{_datadir}/texmf-dist/fonts/type1/public/beuron/beuron.pfb
%{_datadir}/texmf-dist/fonts/type1/public/beuron/beuronc.pfb
%{_datadir}/texmf-dist/fonts/type1/public/beuron/beuronx.pfb
%{_datadir}/texmf-dist/tex/latex/beuron/beuron.sty
%{_datadir}/texmf-dist/tex/latex/beuron/t1beuron.fd
