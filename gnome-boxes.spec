# TODO
# - Requires: qemu is too much (pulls all arches)
Summary:	A simple GNOME 3 application to access remote or virtual systems
Summary(pl.UTF-8):	Prosta aplikacja GNOME 3 do dostępu do systemów zdalnych lub wirtualnych
Name:		gnome-boxes
Version:	48.0
Release:	2
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-boxes/48/%{name}-%{version}.tar.xz
# Source0-md5:	2436442ab2e7b0688338cb41cc8267ea
Patch0:		no-cache-update.patch
URL:		https://apps.gnome.org/Boxes/
BuildRequires:	AppStream
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	gtk-webkit4.1-devel >= 2.36.0
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libhandy1-devel >= 1.5.0
BuildRequires:	libosinfo-devel >= 1.10.0
BuildRequires:	libportal-devel >= 0.7
BuildRequires:	libportal-gtk3-devel >= 0.7
BuildRequires:	libsecret-devel
BuildRequires:	libsoup3-devel >= 3.0.0
BuildRequires:	libusb-devel >= 1.0.9
BuildRequires:	libvirt-glib-devel >= 5.0.0
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	spice-gtk-devel >= 0.32
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	udev-glib-devel >= 1:165
BuildRequires:	vte-devel >= 0.40.2
BuildRequires:	vala >= 2:0.24.0.65
BuildRequires:	vala-libhandy1 >= 1.5.0
BuildRequires:	vala-libosinfo >= 1.10.0
BuildRequires:	vala-libportal >= 0.7
BuildRequires:	vala-libportal-gtk3 >= 0.7
BuildRequires:	vala-libvirt-glib >= 5.0.0
BuildRequires:	vala-spice-gtk >= 0.32
BuildRequires:	vala-tracker3 >= 3.0
BuildRequires:	vala-vte >= 0.40.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50
Requires:	gtk+3 >= 3.22.20
Requires:	gtk-webkit4.1 >= 2.36.0
Requires:	hicolor-icon-theme
Requires:	libarchive >= 3.0.0
Requires:	libhandy1 >= 1.5.0
Requires:	libosinfo >= 1.10.0
Requires:	libportal >= 0.7
Requires:	libportal-gtk3 >= 0.7
Requires:	libsoup3 >= 3.0.0
Requires:	libusb >= 1.0.9
Requires:	libvirt-glib >= 5.0.0
Requires:	libvirt-utils
Requires:	libxml2 >= 1:2.7.8
Requires:	qemu >= 1.3
Requires:	spice-gtk >= 0.32
Requires:	tracker3 >= 3.0
Requires:	udev-glib >= 1:165
Requires:	vte >= 0.40.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# private libraries
%define		_noautoprovfiles	%{_libdir}/gnome-boxes
%define		_noautoreq		libgovf-0.1.so

%description
gnome-boxes is a simple GNOME 3 application to access remote or
virtual systems.

%description -l pl.UTF-8
gnome-boxes to prosta aplikacja GNOME 3 służąca do dostępu do
systemów zdalnych lub wirtualnych.

%prep
%setup -q
%patch -P 0 -p1

%build
%meson \
	-Ddistributor_name='pld-linux' \
	-Ddistributor_version='%{pld_release}'

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# imported subprojects, not for external use
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/gnome-boxes/govf
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/gnome-boxes/pkgconfig
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gnome-boxes/gir-1.0

# not supported by glibc (as of 2.39)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md copyright
%attr(755,root,root) %{_bindir}/gnome-boxes
%dir %{_libdir}/gnome-boxes
%attr(755,root,root) %{_libdir}/gnome-boxes/libgovf-0.1.so
%dir %{_libdir}/gnome-boxes/girepository-1.0
%{_libdir}/gnome-boxes/girepository-1.0/Govf-0.1.typelib
%attr(755,root,root) %{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/gnome-boxes
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_datadir}/metainfo/org.gnome.Boxes.metainfo.xml
%{_desktopdir}/org.gnome.Boxes.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Boxes.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
