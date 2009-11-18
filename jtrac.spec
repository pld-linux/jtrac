# TODO
# - build it from sources

Summary:	Issue-tracking web application
Name:		jtrac
Version:	2.1.0
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/Java/Servlets
Source0:	http://downloads.sourceforge.net/project/j-trac/jtrac/2.1.0/%{name}-%{version}.zip
Source1:	%{name}-context.xml
# Source0-md5:  6254396d33012f65d0886b67287b257b
URL:		http://sourceforge.net/projects/j-trac/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	tomcat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JTrac is a generic issue-tracking web-application that can be easily
customized by adding custom fields and drop-downs. Features include
customizable workflow, field level permissions, e-mail integration,
file attachments and a detailed history view.

%prep
%setup -qn %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_datadir}/%{name},%{_sharedstatedir}/{%{name},tomcat/conf/Catalina/localhost}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
cp %{name}.war $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.war

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
# do not make this file writeable by tomcat. We do not want to allow user to
# undeploy this app via tomcat manager.
%config(noreplace) %{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
%{_datadir}/%{name}
%attr(2775,root,servlet) %dir %{_sharedstatedir}/%{name}
