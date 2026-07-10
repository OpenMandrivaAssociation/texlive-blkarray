%global tl_name blkarray
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.07
Release:	%{tl_revision}.1
Summary:	Extended array and tabular
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/blkarray
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blkarray.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blkarray.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An experimental package which implements an environment, blockarray,
that may be used in the same way as the array or tabular environments of
standard LaTeX, or their extended versions defined in array. If used in
math-mode, blockarray acts like array, otherwise it acts like tabular.
The package implements a new method of defining column types, and also
block and block* environments, for specifying sub-arrays of the main
array. What's more, the \footnote command works inside a blockarray.

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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/blkarray
%dir %{_datadir}/texmf-dist/tex/latex/blkarray
%doc %{_datadir}/texmf-dist/doc/latex/blkarray/README
%doc %{_datadir}/texmf-dist/doc/latex/blkarray/blkarray.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blkarray/blkarray.tex
%{_datadir}/texmf-dist/tex/latex/blkarray/blkarray.sty
