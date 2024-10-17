Name:		texlive-geradwp
Version:	63134
Release:	2
Summary:	Document class for the Cahiers du GERAD series
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/geradwp
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geradwp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geradwp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geradwp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the geradwp class, a class based on
article and compatible with LaTeX. With this class, researchers
at GERAD will be able to write their working paper while
complying to all the presentation standards required by the
Cahiers du GERAD series.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/geradwp
%{_texmfdistdir}/tex/latex/geradwp
%doc %{_texmfdistdir}/doc/latex/geradwp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
