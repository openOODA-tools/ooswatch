Name:           ooswatch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Displays interactive 16-color ANSI and TrueColor terminal swatches.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooswatch
Source0:        ooswatch-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooswatch is a sovereign, capability-bounded PALETTE VIEWER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooswatch
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooswatch-uninstall

%files
/usr/bin/ooswatch
/usr/bin/ooswatch-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
