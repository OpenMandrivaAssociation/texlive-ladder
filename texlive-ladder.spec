Name:		texlive-ladder
Version:	44394
Release:	2
Summary:	Draw simple ladder diagrams using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ladder
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ladder.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ladder.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package permits the creation of simple ladder diagrams
within LaTeX documents. Required packages are tikz, ifthen, and
calc.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ladder
%doc %{_texmfdistdir}/doc/latex/ladder

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
