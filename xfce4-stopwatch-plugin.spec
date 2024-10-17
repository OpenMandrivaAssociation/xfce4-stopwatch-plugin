Summary:	Stopwatch plugin for the Xfce panel
Name:		xfce4-stopwatch-plugin
Version:	0.2.0
Release:	2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-stopwatch-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-stopwatch-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.6
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)

%description
This plugin keeps track of elapsed time.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
