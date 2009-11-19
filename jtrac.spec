# TODO
# - build it from sources

Summary:	Issue-tracking web application
Name:		jtrac
Version:	2.1.0
Release:	1
License:	Apache v2.0
Group:		Networking/Daemons/Java/Servlets
Source0:	http://downloads.sourceforge.net/project/j-trac/jtrac/2.1.0/%{name}-%{version}.zip
# Source0-md5:  6254396d33012f65d0886b67287b257b
Source1:	%{name}-context.xml
Source2:	%{name}.properties
Source3:	%{name}-log4j.properties
URL:		http://sourceforge.net/projects/j-trac/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-sun-jre >= 1.6.0.17
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

unzip -qd jtrac jtrac.war

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_datadir},%{_sharedstatedir}/{%{name},tomcat/conf/Catalina/localhost},/var/log/%{name}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tomcat-context.xml
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.properties
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/log4j.properties
cp -a %{name} $RPM_BUILD_ROOT%{_datadir}/%{name}

ln -s %{_sysconfdir}/%{name}/tomcat-context.xml $RPM_BUILD_ROOT%{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
ln -s %{_sysconfdir}/%{name}/%{name}.properties $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/%{name}.properties
ln -sf %{_sysconfdir}/%{name}/log4j.properties $RPM_BUILD_ROOT%{_datadir}/%{name}/WEB-INF/log4j.properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
%verify(not md5 mtime size) %config(noreplace) %attr(750,root,servlet) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%attr(770,root,servlet) %{_sharedstatedir}/%{name}
%attr(770,root,servlet) /var/log/%{name}
