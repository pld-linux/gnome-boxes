# TODO
# - Requires: qemu is too much (pulls all arches)
Summary:	A simple GNOME 3 application to access remote or virtual systems
Summary(pl.UTF-8):	Prosta aplikacja GNOME 3 do dostępu do systemów zdalnych lub wirtualnych
Name:		gnome-boxes
Version:	3.26.2
Release:	1
License:	LGPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	1c55bcaf57234a9b66136c8811e74876
URL:		http://live.gnome.org/Boxes
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	gtk3-vnc-devel >= 0.4.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libgovirt-devel >= 0.2.0
BuildRequires:	libosinfo-devel >= 0.2.12
BuildRequires:	libsoup-devel >= 2.38.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libusb-devel >= 1.0.9
BuildRequires:	libuuid-devel >= 1.41.3
BuildRequires:	libvirt-glib-devel >= 0.2.2
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	spice-gtk-devel >= 0.27
BuildRequires:	tracker-devel >= 0.14.0
BuildRequires:	udev-glib-devel >= 1:165
BuildRequires:	vala >= 2:0.24.0.65
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.38.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
Requires:	libgovirt >= 0.2.0
Requires:	libosinfo >= 0.2.12
Requires:	libsoup >= 2.38.0
Requires:	libusb >= 1.0.9
Requires:	libuuid >= 1.41.3
Requires:	libvirt-glib >= 0.2.2
Requires:	libvirt-utils
Requires:	libxml2 >= 1:2.7.8
Requires:	qemu >= 1.3
Requires:	spice-gtk >= 0.27
Requires:	tracker >= 0.14.0
Requires:	udev-glib >= 1:165
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-boxes is a simple GNOME 3 application to access remote or
virtual systems.

%description -l pl.UTF-8
gnome-boxes to prosta aplikacja GNOME 3 służąca do dostępu do
systemów zdalnych lub wirtualnych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-smartcard
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnome-boxes
%attr(755,root,root) %{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/appdata/org.gnome.Boxes.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/gnome-boxes
%{_datadir}/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%{_desktopdir}/org.gnome.Boxes.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-boxes.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-boxes-symbolic.svg
