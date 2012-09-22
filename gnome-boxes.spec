# TODO
# - Requires: qemu-kvm is too much (pulls all arches)
Summary:	A simple GNOME 3 application to access remote or virtual systems
Name:		gnome-boxes
Version:	3.4.3
Release:	2
License:	LGPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	6f8a5cf5fddad78d90aa369a7a613c72
URL:		http://live.gnome.org/Boxes
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-gtk-devel >= 1.0.1
BuildRequires:	cogl-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk3-vnc-devel >= 0.4.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libosinfo-devel >= 0.1.1
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libvirt-glib-devel >= 0.0.8
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	spice-gtk-devel >= 0.9
BuildRequires:	tracker-devel >= 0.14.0
BuildRequires:	udev-glib-devel >= 165
BuildRequires:	vala >= 2:0.14.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.30.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+3 >= 3.4.0
Requires:	hicolor-icon-theme
Requires:	libvirt-utils
Requires:	qemu-kvm
Requires:	tracker >= 0.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-boxes is a simple GNOME 3 application to access remote or
virtual systems.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

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
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/gnome-boxes
%{_desktopdir}/gnome-boxes.desktop
%{_iconsdir}/hicolor/*/*/*.png
