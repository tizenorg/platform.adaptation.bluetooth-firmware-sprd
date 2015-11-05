Name:       bluetooth-firmware-sprd
Summary:    firmware and tools for bluetooth
Version:    0.1.1
Release:    0
Group:      TO_BE_FILLED
License:    Apache-2.0
Source0:    bluetooth-firmware-sprd-%{version}.tar.gz
Source1:    bluetooth-hciattach@.service
Source2:    bluetooth-hci-device.service

BuildRequires:  cmake

%if "%{?tizen_profile_name}" == "wearable"
ExcludeArch: %{arm} %ix86 x86_64
%endif

%if "%{?tizen_profile_name}"=="tv"
ExcludeArch: %{arm} %ix86 x86_64
%endif

%description
firmware and tools for bluetooth

%package TM1
Summary:    TM1 firmware and tools for bluetooth
Group:      TO_BE/FILLED

%description TM1
firmware and tools for bluetooth for TM1

%prep
%setup -q -n bluetooth-firmware-sprd-%{version}

%build
export CFLAGS+=" -fpie -fvisibility=hidden"
export LDFLAGS+=" -Wl,--rpath=/usr/lib -Wl,--as-needed -Wl,--unresolved-symbols=ignore-in-shared-libs -pie"

cmake ./ -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPLUGIN_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

install -D -m 0644 %SOURCE1 %{buildroot}%{_libdir}/systemd/system/bluetooth-hciattach@.service
install -D -m 0644 %SOURCE2 %{buildroot}%{_libdir}/systemd/system/bluetooth-hci-device.service
install -D -m 0644 LICENSE %{buildroot}%{_datadir}/license/bluetooth-firmware-sprd-TM1

%post TM1
rm -rf %{_prefix}/etc/bluetooth/bt-dev-start.sh
ln -s %{_prefix}/etc/bluetooth/bt-dev-start-TM1.sh %{_prefix}/etc/bluetooth/bt-dev-start.sh

%files TM1
%defattr(-,root,root,-)
%attr(755,-,-) %{_prefix}/etc/bluetooth/bt-dev-end.sh
%attr(755,-,-) %{_prefix}/etc/bluetooth/bt-dev-start-TM1.sh
%{_datadir}/license/bluetooth-firmware-sprd-TM1
%{_libdir}/systemd/system/bluetooth-hciattach@.service
%{_libdir}/systemd/system/bluetooth-hci-device.service
