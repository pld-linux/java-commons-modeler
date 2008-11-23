#
# Conditional build:
%bcond_without    javadoc        # don't build javadoc

%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Modeler - managing resources via Java Management Extensions
Summary(pl.UTF-8):	Jakarta Commons Modeler - zarządzanie zasobami z użyciem Java Management Extensions
Name:        java-commons-modeler
Version:	2.0
Release:	1
License:	Apache v2.0
Group:        Libraries/Java
Source0:	http://www.apache.org/dist/jakarta/commons/modeler/source/commons-modeler-%{version}-src.tar.gz
# Source0-md5:	43983c66113ddaa9880e4a7ea7d38db4
URL:		http://jakarta.apache.org/commons/modeler/
BuildRequires:	ant
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
BuildRequires:	jdk >= 1.2
BuildRequires:	jmx
BuildRequires:	rpm-javaprov
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-logging
Requires:	jmx
Requires:    jpackage-utils
Requires:	jre >= 1.2
Provides:    jakarta-commons-modeler
Obsoletes:    jakarta-commons-modeler
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This scope of the Modeler component is to provide a class library
supporting the creation and use of Model MBeans to manage application
resources via tools that implement the Java Management Extensions
(JMX) APIs.

%description -l pl.UTF-8
Zadaniem komponentu Modeler jest dostarczenie biblioteki klas
wspierających tworzenie i używanie Model MBeans do zarządzania
zasobami aplikacji z użyciem narzędzi będących implementacją API Java
Management Extensions (JMX).

%package javadoc
Summary:	Jakarta Commons Modeller documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons Modeller
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-modeler-doc

%description javadoc
Jakarta Commons Modeller documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons Modeller.

%prep
%setup -q -n commons-modeler-%{version}-src

%build
required_jars="commons-digester commons-logging jmx"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a dist/commons-modeler.jar $RPM_BUILD_ROOT%{_javadir}/commons-modeler-%{version}.jar
ln -s commons-modeler-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-modeler.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
