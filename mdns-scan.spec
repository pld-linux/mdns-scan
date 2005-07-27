Summary:	scan for mDNS services
Name:		mdns-scan
Version:	0.1
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://0pointer.de/lennart/projects/mdns-scan/%{name}-%{version}.tar.gz
# Source0-md5:	df727b1f56656130d254923d13508be5
URL:		http://0pointer.de/lennart/projects/mdns-scan/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mdns-scan is a tool for scanning for mDNS/DNS-SD published services on
the local network. It issues a mDNS PTR query to the special RR
_services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}
install mdns-scan $RPM_BUILD_ROOT%{_bindir}/mdns-scan

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
