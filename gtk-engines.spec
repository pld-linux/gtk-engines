Summary:	Default GTK+ theme engines
Summary(pl):	Tematy do Gtk+
Name:		gtk-engines
Version:	0.4
Release:	1
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines/%{name}-%{version}.tar.gz
URL:		http://gtk.themes.org/
Requires:	imlib = 1.9.3
Requires:	gtk+ = 1.2.0
Requires:	glib = 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root

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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make exec_prefix=$RPM_BUILD_ROOT/usr/X11R6 prefix=$RPM_BUILD_ROOT/usr/X11R6 install 

strip --strip-debug $RPM_BUILD_ROOT/usr/X11R6/lib/gtk/themes/engines/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog

%dir /usr/X11R6/lib/gtk/themes
%dir /usr/X11R6/lib/gtk/themes/engines
%attr(755,root,root) /usr/X11R6/lib/gtk/themes/engines/lib*so
/usr/X11R6/lib/gtk/themes/engines/lib*la

/usr/X11R6/share/themes

%changelog
* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4-1]
- Updated Requires (gtk = 1.2.0, glib = 1.2.0, imlib = 1.9.3).

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1-2]
- added -q %setup parameter,
- added "Requires: gnome-libs = 0.99.2, gtk = 1.1.12, glib = 1.1.12"
- added LDFLAGS="-s" to ./configure enviroment,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- added --disable-static to configure parameters,
- added stripping gtk themes modules,
- uncommented %clean,
- added pl translation,
- directories in /usr/X11R6/share/themes/ also must belongs
  to package,
- prefix changed to /usr/X11R6.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- in preparation for GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- First try at a spec file
