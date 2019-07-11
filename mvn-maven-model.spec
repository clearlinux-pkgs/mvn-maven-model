#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-model
Version  : 2.0.5
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.pom
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.6/maven-model-2.0.6.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.8/maven-model-2.0.8.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.9/maven-model-2.0.9.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0.9/maven-model-2.0.9.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.0/maven-model-2.0.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.jar
Source10  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.jar
Source12  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.0.4/maven-model-3.0.4.jar
Source14  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.0.4/maven-model-3.0.4.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.0/maven-model-3.0.jar
Source16  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.0/maven-model-3.0.pom
Source17  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.6.0/maven-model-3.6.0.jar
Source18  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.6.0/maven-model-3.6.0.pom
Source19  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.6.1/maven-model-3.6.1.jar
Source20  : https://repo1.maven.org/maven2/org/apache/maven/maven-model/3.6.1/maven-model-3.6.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-model-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-model package.
Group: Data

%description data
data components for the mvn-maven-model package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.8
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.8

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.5/maven-model-2.0.5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.6/maven-model-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.7/maven-model-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.8/maven-model-2.0.8.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9/maven-model-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0.9/maven-model-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.0/maven-model-2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.0/maven-model-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4/maven-model-3.0.4.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0.4/maven-model-3.0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0/maven-model-3.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.0/maven-model-3.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0/maven-model-3.6.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.0/maven-model-3.6.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1/maven-model-3.6.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-model/3.6.1/maven-model-3.6.1.pom
