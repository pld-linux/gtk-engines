Summary:	Default GTK+ theme engines
Summary(pl):	Tematy do Gtk+
Name:		gtk-engines
Version:	0.12
Release:	5
Epoch:		1
License:	GPL
Group:		Themes/Gtk
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gtk-engines/%{name}-%{version}.tar.gz
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.1.13
BuildRequires:	imlib-devel >= 1.8
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
These are the graphical engines for the various GTK+ toolkit themes.
Included themes are:
 - Motif
 - win95
 - Pixmap
 - Raleigh
 - Metal (Java swing-like)

%description -l pl
Pakiet ten zawiera modu�y temat�w do biblioteki Gtk+ o nast�puj�cych
wygl�dach:
 - Motif
 - win95
 - Pixmap
 - Raleigh
 - Metal (Java swing-like)

%prep
%setup -q

%build
rm -f acinclude.m4 missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%{_datadir}/themes/Pixmap
%{_datadir}/themes/Metal
%{_datadir}/themes/Notif
%{_datadir}/themes/Raleigh
%{_datadir}/themes/Redmond95