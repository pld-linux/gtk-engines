Summary:	Default GTK+ theme engines
Summary(pl):	Tematy do Gtk+
Name:		gtk-engines
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gtk-engines/%{name}-%{version}.tar.gz
URL:		http://gtk.themes.org/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.1.13
BuildRequires:	glib-devel >= 1.1.13
BuildRequires:	imlib-devel >= 1.8
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
These are the graphical engines for the various GTK+ toolkit themes.
Included themes are:
 - Motif
 - win95
 - Pixmap
 - Metal (Java swing-like)

%description
Pakiet ten zawiera modu³y tematów do biblioteki Gtk+ o nastêpuj±cych
wygl±dach:
 - Motif
 - win95
 - Pixmap
 - Metal (Java swing-like)

%prep
%setup -q

%build
export LDFLAGS="-s"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines/lib*.so

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.la

%{_datadir}/themes/Pixmap/*
%{_datadir}/themes/Metal
%{_datadir}/themes/Notif
%{_datadir}/themes/Redmond95
