%global tl_name ladder
%global tl_revision 44394

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw simple ladder diagrams using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/ladder
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ladder.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ladder.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package permits the creation of simple ladder diagrams within LaTeX
documents. Required packages are tikz, ifthen, and calc.

