%define oname	python-mate
%define oldname mate-python

#no mate ports
%define	build_brasero		0
%define	build_atril		0
%define	build_print		0
%define	build_mediaprofiles	0

Summary:	MATE Desktop bindings for Python
Name:		python-mate-desktop
Version:	1.2.0
Release:	2
License:	LGPLv2+ and GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(atril-document-2.32)
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	pkgconfig(libcaja-extension)
#BuildRequires:	pkgconfig(libmateprintui-2.2)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmarco-private)
BuildRequires:	pkgconfig(libmateui-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-3.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-keyring-1)
BuildRequires:	pkgconfig(mate-media-profiles)
BuildRequires:	pkgconfig(mate-python-2.0)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pymatecorba-2)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(totem-plparser)

Requires:	mate-desktop

%description
The mate-python-desktop package contains the Python bindings for the
MATE Desktop modules.

%package -n %{oname}-applet 	 
Summary:	Python bindings for MATE Panel applets
Group:		Graphical desktop/GNOME
Requires:	mate-panel
Requires:	python-mate
Obsoletes:	%{oldname}-applet

%description -n %{oname}-applet
This module contains a wrapper that allows MATE Panel applets to be
written in Python.

%if %{build_atril}
%package -n %{oname}-atril
Summary:	Python bindings for the Atril document viewer
Group:		Graphical desktop/GNOME
Requires:	atril

%description -n %{oname}-atril
This module contains a wrapper that makes the Atril document viewer library
available from Python.
%endif

%if %{build_brasero}
%package -n %{oname}-brasero
Summary:	Python bindings for Brasero
Group:		Graphical desktop/GNOME
Requires:	brasero
BuildRequires:	brasero-devel

%description -n %{oname}-brasero
This module contains a wrapper that makes Brasero available from Python.
%endif

%package -n %{oname}-gtksourceview
Summary:	Python bindings for Gtksourceview
Group:		Graphical desktop/GNOME
Requires:	gtksourceview1
Requires:	%{oname}-print = %{version}

%description -n %{oname}-gtksourceview
This module contains a wrapper that makes Gtksourceview available from Python.

%package -n %{oname}-gtop
Summary:	Python bindings for Gtop
Group:		Graphical desktop/GNOME
Requires:	libgtop2
Obsoletes:	%{oldname}-gtop

%description -n %{oname}-gtop
This module contains a wrapper that makes Gtop available from Python.

%package -n %{oname}-marco
Summary:	Python bindings for the Marco window manager
Group:		Graphical desktop/GNOME
#marco isnt a provide yet
Requires:	mate-window-manager 
Obsoletes:	%{oldname}-marco

%description -n %{oname}-marco
This module contains a wrapper that makes the Marco window manager library
available from Python.

%package -n %{oname}-keyring
Summary:	Python bindings for mate-keyring
Group:		Graphical desktop/GNOME
Requires:	mate-keyring
Obsoletes:	%{oldname}-matekeyring

%description -n %{oname}-keyring
This module contains a wrapper that makes mate-keyring available from Python.

%if %{build_mediaprofiles}
%package -n %{oname}-mediaprofiles
Summary:	Python bindings for the MATE media profiles
Group:		Graphical desktop/GNOME
Requires:	mate-media
Requires:	python-mateconf
BuildRequires:	pkgconfig(mate-media-profiles)

%description -n %{oname}-mediaprofiles
This module contains a wrapper that makes the MATE media profiles library
available from Python.
%endif

%if %{build_print}
%package -n %{oname}-print
Summary:	Python bindings for interacting with mateprint and mateprintui
Group:		Graphical desktop/GNOME
Requires:	libmateprintui
Requires:	python-matecanvas
BuildRequires:	libmateprintui-devel >= 2.8.0

%description -n %{oname}-print
This module contains a wrapper that allows the use of mateprint and
mateprintui via python.
%endif

%package -n %{oname}-rsvg
Summary:	Python bindings for Rsvg
Group:		Graphical desktop/GNOME
Requires:	librsvg2
Obsoletes:	%{oldname}-rsvg

%description -n %{oname}-rsvg
This module contains a wrapper that makes Rsvg available from Python.

%package -n %{oname}-totem
Summary:	Python bindings for the Totem playlist parser
Group:		Graphical desktop/GNOME
Obsoletes:	%{oldname}-totem

%description -n %{oname}-totem
This module contains a wrapper that makes the Totem playlist parser
available from Python.

%package -n %{oname}-wnck
Summary:	Python-wnck bindings
Group:		Graphical desktop/GNOME
Requires:	libwnck
Obsoletes:	%{oldname}-wnck

%description -n %{oname}-wnck
This package contains a module that allows communication with the Window
Manager using the EWMH specification from Python applications.

%package devel
Summary:	Pkgconfig file for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}

%description devel
This package contains pkgconfig file for %{name}.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--enable-marco \
	--disable-gtksourceview

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm {} \;

%files
%doc AUTHORS ChangeLog
%{py_platsitedir}/gtk-2.0/matedesktop/
%{py_platsitedir}/gtk-2.0/bugbuddy* 

%files -n %{oname}-applet
%doc examples/applet/
%{py_platsitedir}/gtk-2.0/mate/applet.py*
%{py_platsitedir}/gtk-2.0/mateapplet.so

%if %{build_atril}
%files -n %{oname}-atril
%{py_platsitedir}/gtk-2.0/atril.so
%endif

%if 0
%files -n %{oname}-gtksourceview
%doc examples/gtksourceview
%{py_platsitedir}/gtk-2.0/gtksourceview.so
%doc %{_datadir}/gtk-doc/html/pygtksourceview
%endif

%files -n %{oname}-gtop
%{py_platsitedir}/gtk-2.0/gtop.so

%if %{build_brasero}
%files -n %{oname}-brasero
%doc examples/brasero*
%{py_platsitedir}/gtk-2.0/braseroburn.so
%{py_platsitedir}/gtk-2.0/braseromedia.so
%doc examples/braseromedia
%endif

%files -n %{oname}-keyring
%doc examples/keyring*
%{py_platsitedir}/gtk-2.0/matekeyring.so

%if %{build_print}
%files -n %{oname}-print
%doc examples/mateprint/
%{py_platsitedir}/gtk-2.0/mateprint/
%{_datadir}/gtk-doc/html/pymateprint*
%endif

%if %{build_mediaprofiles}
%files -n %{oname}-mediaprofiles
%doc examples/mediaprofiles
%{py_platsitedir}/gtk-2.0/mediaprofiles.so
%endif

%files -n %{oname}-marco
%{py_platsitedir}/gtk-2.0/marco.so

%files -n %{oname}-rsvg
%doc examples/rsvg
%{py_platsitedir}/gtk-2.0/rsvg.so

%files -n %{oname}-totem
%{py_platsitedir}/gtk-2.0/totem/

%files -n %{oname}-wnck
%doc examples/wnck*
%{py_platsitedir}/gtk-2.0/wnck.so

%files devel
%{_libdir}/pkgconfig/%{oname}-desktop-2.0.pc
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/_matedesktop.defs
%{_datadir}/pygtk/2.0/defs/applet.defs
%{_datadir}/pygtk/2.0/defs/matekeyring.defs
#{_datadir}/pygtk/2.0/defs/gtksourceview.defs
#{_datadir}/pygtk/2.0/defs/mediaprofiles.defs
%{_datadir}/pygtk/2.0/defs/marco.defs
#{_datadir}/pygtk/2.0/defs/print.defs
#{_datadir}/pygtk/2.0/defs/printui.defs
#{_datadir}/pygtk/2.0/defs/atril.defs
%{_datadir}/pygtk/2.0/defs/wnck.defs

