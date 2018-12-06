%global goipath  github.com/dsnet/golib
%global commit   1ea1667757804fdcccc5a1810e09aba618885ac2
Version: 0

%global common_description %{expand:
This repository stores a collection of mostly unrelated helper libraries.
Functionality that the author (Joe Tsai) found common among his various projects
are pulled out and placed here.}

%gometa

Name: %{goname}
Release: 0.2%{?dist}
Summary: Collection of helper libraries for Go
License: BSD
URL: %{gourl}
Source0: %{gosource}
BuildRequires: golang(github.com/google/go-cmp/cmp)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE.md
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git1ea1667
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180326git1ea1667
- First package for Fedora
