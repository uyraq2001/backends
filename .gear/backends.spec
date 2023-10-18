%define _unpackaged_files_terminate_build 1

Name: backends
Version: 0.1.0
Release: alt1

Summary: Backend files for Alterator Browser
License: GPLv2+
Group: Other
URL: https:/github.com/uyraq2001/backends


Source0: %name-%version.tar

%description
Backend files for Alterator Browser

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
* Wed Oct 18 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
