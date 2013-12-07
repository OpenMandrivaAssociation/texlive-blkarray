# revision 17089
# category Package
# catalog-ctan /macros/latex/contrib/blkarray
# catalog-date 2010-02-23 16:09:16 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-blkarray
Version:	20100223
Release:	3
Summary:	Extended array and tabular
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blkarray
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blkarray.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blkarray.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An experimental package which implements an environment,
blockarray, that may be used in the same way as the array or
tabular environments of standard LaTeX, or their extended
versions defined in array. If used in math-mode, blockarray
acts like array, otherwise it acts like tabular. The package
implements a new method of defining column types, and also
block and block* environments, for specifying sub-arrays of the
main array. What's more, the \footnote command works inside a
blockarray.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/blkarray/blkarray.sty
%doc %{_texmfdistdir}/doc/latex/blkarray/README
%doc %{_texmfdistdir}/doc/latex/blkarray/blkarray.pdf
%doc %{_texmfdistdir}/doc/latex/blkarray/blkarray.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100223-2
+ Revision: 749768
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100223-1
+ Revision: 717953
- texlive-blkarray
- texlive-blkarray
- texlive-blkarray
- texlive-blkarray
- texlive-blkarray

