Summary:	Stopwatch plugin for the Xfce panel
Name:		xfce4-stopwatch-plugin
Version:	0.2.0
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-stopwatch-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-stopwatch-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.6
BuildRequires:	xfce4-panel-devel >= 4.6
BuildRequires:	libxfcegui4-devel >= 4.6
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin keeps track of elapsed time.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
%__rm -rf  %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
