Summary:	Default GTK+ theme engines
Summary(pl):	Motywy do Gtk+
Name:		gtk-engines
Version:	0.12
Release:	8
Epoch:		1
License:	GPL
Group:		Themes/GTK+
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c867d1ebd6dbea355765d689a11330ec
Patch0:		%{name}-memleak.patch
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.1.13
BuildRequires:	imlib-devel >= 1.8
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the graphical engines for the various GTK+ toolkit themes.
Included themes are:
 - Motif
 - win95
 - Pixmap
 - Raleigh
 - Metal (Java swing-like)

%description -l pl
Pakiet ten zawiera modu³y motywów do biblioteki Gtk+ o nastêpuj±cych
wygl±dach:
 - Motif
 - win95
 - Pixmap
 - Raleigh
 - Metal (Java swing-like)

%prep
%setup -q
%patch0 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
%{_datadir}/themes/Pixmap
%{_datadir}/themes/Metal/*
%{_datadir}/themes/Notif
%{_datadir}/themes/Raleigh
%{_datadir}/themes/Redmond95
