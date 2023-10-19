%define _unpackaged_files_terminate_build 1

Name: alterator-browser-backends
Version: 0.1.0
Release: alt2

Summary: Backend files for ACC
License: GPLv2+
Group: Other
URL: https:/github.com/uyraq2001/backends
BuildArch: noarch

Source0: %name-%version.tar

%description
Backend files for alterator control center modules, using by Alterator Browser

%prep
%setup

%install
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/scripts

install -v -p -m 644 -D  backends/*.backend %buildroot%_datadir/alterator/backends
install -v -p -m 644 -D  scripts/*.sh %buildroot%_datadir/alterator/scripts

%files
%_datadir/alterator/backends/*.backend
%_datadir/alterator/scripts/*.sh

%changelog
* Thu Oct 19 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt2
- change spec file

* Wed Oct 18 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
