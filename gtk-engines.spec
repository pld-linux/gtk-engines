Summary:	Default GTK+ theme engines
Summary(pl):	Tematy do Gtk+
Name:		gtk-engines
Version:	0.5
Release:	1
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines/%{name}-%{version}.tar.gz
URL:		http://gtk.themes.org/
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
./configure %{_target_platform} \
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
