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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An experimental package which implements an environment, blockarray,
that may be used in the same way as the array or tabular environments of
standard LaTeX, or their extended versions defined in array. If used in
math-mode, blockarray acts like array, otherwise it acts like tabular.
The package implements a new method of defining column types, and also
block and block* environments, for specifying sub-arrays of the main
array. What's more, the \footnote command works inside a blockarray.

