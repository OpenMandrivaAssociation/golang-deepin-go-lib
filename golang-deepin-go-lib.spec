%define   _name           go-lib
%define   import_path     github.com/linuxdeepin/go-lib

Name:           golang-github-linuxdeepin-go-lib
Version:        6.0.6
Release:        1
Summary:        Go bindings for Deepin Desktop Environment development
License:        GPL-3.0-or-later
Group:          Development/Languages/Golang
URL:            https://github.com/linuxdeepin/go-lib
Source0:        https://github.com/linuxdeepin/go-lib/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# The development package of golang is named *-source, please skip this rpmlint elibX11-1rror.
Source99:       golang-github-linuxdeepin-go-lib-rpmlintrc
BuildRequires:  fdupes
# BuildRequires:  golang-github-linuxdeepin-go-x11-client
BuildRequires:  golang-packaging
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  pam-devel
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
# Requires:       golang-github-linuxdeepin-go-x11-client
Requires:       golang(github.com/linuxdeepin/go-gir/gio-2.0)
Requires:       golang(github.com/linuxdeepin/go-gir/glib-2.0)
%{go_provides}

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%prep
%setup -q -a1 -n %{_name}-%{version}

%build
export GO111MODULE=off
export CGO_ENABLED=1
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/blur.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/gaussianiir2d.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/gdk_pixbuf_utils.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/pulse/dde-pulse.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pulse/
install -m 0644 %{_builddir}/go/src/%{import_path}/pulse/meter.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pulse/
install -m 0644 %{_builddir}/go/src/%{import_path}/sound/player.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/sound/
# install -m 0644 %{_builddir}/go/src/%{import_path}/sound_effect/wav.c \
#                 %{buildroot}%{go_contribsrcdir}/%{import_path}/sound_effect/
install -m 0644 %{_builddir}/go/src/%{import_path}/stb_vorbis/stb_vorbis.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/stb_vorbis/
install -m 0644 %{_builddir}/go/src/%{import_path}/pam/transaction.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pam/
# install -m 0644 %{_builddir}/go/src/%{import_path}/gm/sm2/dde-sm2.c \
#                 %{buildroot}%{go_contribsrcdir}/%{import_path}/gm/sm2/
rm -rf %{buildroot}%{go_contribsrcdir}/%{import_path}/vendor
%gofilelist

%fdupes %{buildroot}

%files -f file.lst
%defattr(-,root,root)
%doc README.md
%license LICENSE
