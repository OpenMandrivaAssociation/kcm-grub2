Name:           kcm-grub2
Requires:       grub2
License:        GPLv3+
Url:            http://ksmanis.wordpress.com/projects/grub2-editor/
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for configuring the GRUB2 bootloader
Version:        0.5.5
Release:        1
Source:         %{name}-%{version}.tar.gz
BuildRequires:  kdelibs4-devel
BuildRequires:  pkgconfig(hwinfo)
BuildRequires:  pkgconfig(ImageMagick)

%description
Smoothly integrated in KDE System Settings, it is the central place 
for managing your GRUB2 configuration.

%files -f %name.lang
%doc COPYING README
%{_kde_datadir}/kde4/services/kcm_grub2.desktop
%{_kde_libdir}/kde4/kcm_grub2.so
%{_kde_libdir}/kde4/libexec/kcmgrub2helper
%config %{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name
