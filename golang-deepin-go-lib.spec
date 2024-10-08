%undefine _debugsource_packages
%define   _name           go-lib
%define   goipath     github.com/linuxdeepin/go-lib

Name:           golang-deepin-go-lib
Version:        6.0.6
Release:        3
Summary:        Go bindings for Deepin Desktop Environment development
License:        GPL-3.0-or-later
Group:          Development/Languages/Golang
URL:            https://github.com/linuxdeepin/go-lib
Source0:        https://github.com/linuxdeepin/go-lib/archive/%{version}/%{_name}-%{version}.tar.gz
# Generated by running, inside the source tree:
# export GOPATH=$(pwd)/.godeps
# go mod download
# tar cJf ../../godeps-for-go-libs-6.0.6.tar.xz .godeps
Source1:	godeps-for-go-libs-6.0.6.tar.xz

BuildRequires:  fdupes
BuildRequires:  golang-github-linuxdeepin-go-x11-client
BuildRequires:  golang
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  pam-devel
BuildRequires:	compiler(go-compiler)
BuildRequires:  golang(github.com/linuxdeepin/go-gir/gio-2.0)
BuildRequires:  golang(github.com/linuxdeepin/go-gir/glib-2.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
BuildArch:      noarch
Requires:       golang-github-linuxdeepin-go-x11-client
Requires:       golang(github.com/linuxdeepin/go-gir/gio-2.0)
Requires:       golang(github.com/linuxdeepin/go-gir/glib-2.0)

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%prep
%autosetup -p1 -a1 -n %{_name}-%{version}

%build
export GOPATH=$(pwd)/.godeps:$(pwd)/gopath

go generate
go build
# FIXME we should probably run `make test`, but it requires a number
# of additional go libraries that don't seem to be caught by
# `go download`.

%install
%goinstall

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/gocode/src/%{goipath}
