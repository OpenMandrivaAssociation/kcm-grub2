# These macros are not present on the target distribution and are provided explicitly here
%define _kde4_configkcfgdir %{_kde4_sharedir}/config.kcfg
%define getres kcm-grub2-getres

Summary:	A KDE Control Module for configuring the GRUB2 bootloader
Name:		kcm-grub2
Version:	0.6.4
Release:	5
License:	GPLv3+
Url:		http://ksmanis.wordpress.com/projects/grub2-editor/
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.gz
Source1:	get_res.cpp
Source2:	%{name}.po
Patch0:		kcm-grub2-read-mode-from-file.patch
BuildRequires:	gcc-c++
BuildRequires:	kdelibs4-devel 
BuildRequires:	pkgconfig(hwinfo)
BuildRequires:	pkgconfig(ImageMagick)
Requires:	grub2

%description
Smoothly integrated in KDE System Settings, it is the central place 
for managing your GRUB2 configuration.

%prep
%setup -q
cp -f %{SOURCE2} ./po/ru/kcm-grub2.po
%apply_patches
g++ %{SOURCE1} -l hd -o %{getres}

%build
#%cmake_kde4 -d ..
%cmake_kde4
cd .. && %make

%install
#%kde4_makeinstall -C build
#kde_post_install
#rm -fr %{buildroot}
make -C build DESTDIR=%{buildroot} install
%find_lang %{name}
install -d %{buildroot}%{_sbindir}
install -m 700 %{getres} %{buildroot}%{_sbindir}/%{getres}

%post
%{_sbindir}/%{getres}

%files -f %{name}.lang
%doc COPYING README
%{_datadir}/kde4/services/kcm_grub2.desktop
%{_kde_libdir}/kde4/kcm_grub2.so
%{_kde_libdir}/kde4/libexec/kcmgrub2helper
%config %{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%{_sbindir}/%{getres}

