# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

%define _kde4_configkcfgdir %{_kde4_sharedir}/config.kcfg

Name:           kcm-grub2
Requires:       grub2
BuildRequires:  gcc-c++
BuildRequires:  kdelibs4-devel 
BuildRequires:  libhd-devel
BuildRequires:  libmagick-devel
License:        GPLv3+
Url:            http://ksmanis.wordpress.com/projects/grub2-editor/
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A KDE Control Module for configuring the GRUB2 bootloader
Version:        0.5.5
Release:        1
Source:         %{name}-%{version}.tar.gz
#%kde4_runtime_requires

%description
Smoothly integrated in KDE System Settings, it is the central place 
for managing your GRUB2 configuration.

Author(s):
  Konstantinos Smanis <konstantinos.smanis@gmail.com>


%prep
%setup -n %{name}-%{version} -q

%build
#%cmake_kde4 -d ..
%cmake_kde4
cd .. && %make
#%make_jobs

%install
#%kde4_makeinstall -C build
#kde_post_install
#rm -fr %buildroot
make -C build DESTDIR=%buildroot install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%{_datadir}/kde4/services/kcm_grub2.desktop
%{_kde_libdir}/kde4/kcm_grub2.so
%{_kde_libdir}/kde4/libexec/kcmgrub2helper
%config %{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
