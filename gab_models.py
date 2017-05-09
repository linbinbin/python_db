# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Index, String, Table, Unicode, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class COMPANY(Base):
    __tablename__ = 'COMPANY'

    l = Column(String(3), nullable=False, server_default=text("''"))
    c = Column(String(2))
    companyCode = Column(String(10), primary_key=True, server_default=text("''"))
    oldCompanyCode = Column(String(6))
    company = Column(String(100))
    localCompany = Column(Unicode(100))
    jpYomiCompany = Column(String(160))
    companyDisc = Column(String(4), nullable=False, server_default=text("''"))
    connectiveType = Column(String(1))
    companyPostalCode = Column(String(20))
    companyPostalAddress = Column(String(120))
    companyLocalPostalAddress = Column(Unicode(120))
    companyTelephoneNumber = Column(String(20))
    chargeSn = Column(String(40))
    chargeGivenName = Column(String(40))
    chargeMail = Column(String(100))
    tempPassword = Column(String(15))
    registerStatus = Column(String(1))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperCompany = Column(String(100))
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)
    flagnet23 = Column(String(1))
    net23DataPath = Column(String(100))


class GLOBALCOMPANY(Base):
    __tablename__ = 'GLOBALCOMPANY'

    globalCompanyCode = Column(String(32), nullable=False, server_default=text("''"))
    companyCode = Column(String(10), primary_key=True, server_default=text("''"))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperGlobalCompanyCode = Column(String(32))


class GLOBALFUNCTION(Base):
    __tablename__ = 'GLOBALFUNCTION'

    globalFunctionCode = Column(String(32), primary_key=True, server_default=text("''"))
    globalFunctionName = Column(String(100))
    localGlobalFunctionName = Column(String(100))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    NMLOnlyFlag = Column(String(1))


class OFFICE(Base):
    __tablename__ = 'OFFICE'

    companyCode = Column(String(10), primary_key=True, nullable=False, server_default=text("''"))
    localOfficeCode = Column(String(4), primary_key=True, nullable=False, server_default=text("''"))
    officeName = Column(String(100))
    localOfficeName = Column(Unicode(100))
    officePostalCode = Column(String(20))
    officePostalAddress = Column(String(120))
    localOfficePostalAddress = Column(Unicode(120))
    officeTelephoneNumber = Column(String(20))
    timeZone = Column(String(20))
    summerTime = Column(String(5))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperOfficeName = Column(String(100))
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ORGANIZATION(Base):
    __tablename__ = 'ORGANIZATION'

    companyCode = Column(String(10), primary_key=True, nullable=False, server_default=text("''"))
    localOuCode = Column(String(6), primary_key=True, nullable=False, server_default=text("''"))
    globalFunctionCode = Column(String(32))
    localOperationDivisionCode = Column(String(6))
    operationDivisionName = Column(String(255))
    localOperationDivisionName = Column(Unicode(128))
    localDivisionCode = Column(String(6))
    divisionName = Column(String(255))
    localDivisionName = Column(Unicode(128))
    localDepartmentCode = Column(String(6))
    departmentName = Column(String(255))
    localDepartmentName = Column(Unicode(128))
    localSectionCode = Column(String(6))
    sectionName = Column(String(255))
    localSectionName = Column(Unicode(128))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperOu = Column(String(255))
    ou = Column(String(255))
    localOu = Column(Unicode(255))
    upperGlobalFunctionCode = Column(String(32))
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class PERSON(Base):
    __tablename__ = 'PERSON'
    __table_args__ = (
        Index('PERSON_IDX_12', 'localOu', 'companyCode', 'uid'),
        Index('PERSON_IDX_17', 'companyCode', 'localOuCode', 'globalFunctionCode', 'employmentType', 'uid'),
        Index('PERSON_IDX_9', 'localOuCode', 'companyCode', 'uid', 'titleLevel'),
        Index('PERSON_IDX_5', 'jpYomiGivenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_4', 'givenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_3', 'localSn', 'companyCode', 'uid'),
        Index('PERSON_IDX_8', 'upperGivenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_7', 'upperSn', 'upperGivenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_11', 'localOfficeCode', 'companyCode', 'uid'),
        Index('PERSON_IDX_6', 'localGivenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_2', 'jpYomiSn', 'companyCode', 'uid'),
        Index('PERSON_IDX_10', 'flagResource', 'directoryReflectEndDate', 'uid'),
        Index('PERSON_IDX_1', 'sn', 'givenName', 'companyCode', 'uid'),
        Index('PERSON_IDX_13', 'upperOu', 'companyCode', 'uid')
    )

    uid = Column(String(15), nullable=False, server_default=text("''"))
    companyCode = Column(String(10), primary_key=True, nullable=False, server_default=text("''"))
    employeeNumber = Column(String(10), primary_key=True, nullable=False, server_default=text("''"))
    locale = Column(String(2))
    sn = Column(String(40), nullable=False, server_default=text("''"))
    givenName = Column(String(40))
    middleName = Column(String(40))
    localSn = Column(Unicode(40))
    localGivenName = Column(Unicode(40))
    localMiddleName = Column(Unicode(40))
    jpYomiSn = Column(String(40))
    jpYomiGivenName = Column(String(40))
    managerUid = Column(String(15))
    net23MailAddress = Column(String(100), index=True)
    mail = Column(String(100), index=True)
    localMailAddress = Column(String(100))
    mobile = Column(String(20))
    pager = Column(String(20))
    telephoneNumber = Column(String(20))
    telephoneNumber2 = Column(String(20))
    telephoneNumber3 = Column(String(20))
    extensionNumber = Column(String(20))
    extensionNumber2 = Column(String(20))
    extensionNumber3 = Column(String(20))
    facsimileTelephoneNumber = Column(String(20))
    extensionFacsimileNumber = Column(String(20))
    employmentType = Column(String(1))
    contractorCode = Column(String(10))
    teamCode = Column(String(4))
    description = Column(String(120))
    localDescription = Column(Unicode(120))
    localOuCode = Column(String(6))
    ou = Column(String(255))
    localOu = Column(Unicode(255))
    localTitleCode = Column(String(2))
    title = Column(String(80))
    localTitle = Column(Unicode(80))
    rankCode = Column(String(2))
    titleLevel = Column(String(1))
    localOfficeCode = Column(String(4))
    expirationDate = Column(DateTime)
    expirationMailFlag = Column(String(1))
    idCardNumber = Column(String(8))
    globalBusinessCode = Column(String(2))
    globalFunctionCode = Column(String(32))
    flagResource = Column(String(1))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperSn = Column(String(40))
    upperGivenName = Column(String(40))
    upperMiddleName = Column(String(40))
    upperGlobalFunctionCode = Column(String(32))
    upperOu = Column(String(255))
    upperTitle = Column(String(80))
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime, index=True)


class PERSONAPPLY(Base):
    __tablename__ = 'PERSONAPPLY'

    applyRequestNumber = Column(BigInteger, primary_key=True, server_default=text("(0)"))
    applyType = Column(String(1), nullable=False, server_default=text("''"))
    applyStatus = Column(String(1), nullable=False, server_default=text("''"))
    applyUid = Column(String(15), nullable=False, server_default=text("''"))
    applyDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    applyMailFlag = Column(String(1), nullable=False, server_default=text("''"))
    approvalUid = Column(String(15), nullable=False, server_default=text("''"))
    approvalDate = Column(DateTime)
    approvalMailFlag = Column(String(1))
    deleteDate = Column(DateTime)
    uid = Column(String(15), nullable=False, server_default=text("''"))
    companyCode = Column(String(10), nullable=False, server_default=text("''"))
    employeeNumber = Column(String(10), nullable=False, server_default=text("''"))
    locale = Column(String(2))
    sn = Column(String(40), nullable=False, server_default=text("''"))
    givenName = Column(String(40))
    middleName = Column(String(40))
    localSn = Column(Unicode(40))
    localGivenName = Column(Unicode(40))
    localMiddleName = Column(Unicode(40))
    jpYomiSn = Column(String(40))
    jpYomiGivenName = Column(String(40))
    managerUid = Column(String(15))
    net23MailAddress = Column(String(100))
    mail = Column(String(100))
    localMailAddress = Column(String(100))
    mobile = Column(String(20))
    pager = Column(String(20))
    telephoneNumber = Column(String(20))
    telephoneNumber2 = Column(String(20))
    telephoneNumber3 = Column(String(20))
    extensionNumber = Column(String(20))
    extensionNumber2 = Column(String(20))
    extensionNumber3 = Column(String(20))
    facsimileTelephoneNumber = Column(String(20))
    extensionFacsimileNumber = Column(String(20))
    employmentType = Column(String(1))
    contractorCode = Column(String(10))
    teamCode = Column(String(4))
    description = Column(String(120))
    localDescription = Column(Unicode(120))
    localOuCode = Column(String(6))
    ou = Column(String(255))
    localOu = Column(Unicode(255))
    localTitleCode = Column(String(2))
    title = Column(String(80))
    localTitle = Column(Unicode(80))
    rankCode = Column(String(2))
    titleLevel = Column(String(1))
    localOfficeCode = Column(String(4))
    expirationDate = Column(DateTime)
    expirationMailFlag = Column(String(1))
    idCardNumber = Column(String(8))
    globalBusinessCode = Column(String(2))
    globalFunctionCode = Column(String(32))
    tempPassword = Column(String(15))
    flagResource = Column(String(1))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class POST(Base):
    __tablename__ = 'POST'

    companyCode = Column(String(10), primary_key=True, nullable=False, server_default=text("''"))
    localTitleCode = Column(String(2), primary_key=True, nullable=False, server_default=text("''"))
    title = Column(String(80))
    localTitle = Column(Unicode(80))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    upperTitle = Column(String(80))
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLE(Base):
    __tablename__ = 'ROLE'

    roleId = Column(String(6), primary_key=True, server_default=text("''"))
    roleName = Column(String(50), nullable=False, server_default=text("''"))
    localRoleName = Column(String(50), nullable=False, server_default=text("''"))
    roleLevel = Column(String(1), nullable=False, server_default=text("''"))
    roleType = Column(String(1), nullable=False, server_default=text("''"))
    openDirectory = Column(String(1), nullable=False, server_default=text("''"))
    openPortal = Column(String(1), nullable=False, server_default=text("''"))
    ownerUid = Column(String(15))
    roleTermTo = Column(DateTime)
    warningMailFlag = Column(String(1))
    condition1Field = Column(String(50))
    condition1Operator = Column(String(10))
    condition1Value = Column(String(50))
    condition2Field = Column(String(50))
    condition2Operator = Column(String(10))
    condition2Value = Column(String(50))
    condition3Field = Column(String(50))
    condition3Operator = Column(String(10))
    condition3Value = Column(String(50))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLEAPPLY(Base):
    __tablename__ = 'ROLEAPPLY'

    applyRequestNumber = Column(BigInteger, primary_key=True, server_default=text("(0)"))
    applyType = Column(String(1), nullable=False, server_default=text("''"))
    applyStatus = Column(String(1), nullable=False, server_default=text("''"))
    applyUid = Column(String(15), nullable=False, server_default=text("''"))
    applyDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    applyMailFlag = Column(String(1), nullable=False, server_default=text("''"))
    approvalUid = Column(String(15), nullable=False, server_default=text("''"))
    approvalDate = Column(DateTime)
    approvalMailFlag = Column(String(1))
    deleteDate = Column(DateTime)
    roleId = Column(String(6), nullable=False, server_default=text("''"))
    roleName = Column(String(50), nullable=False, server_default=text("''"))
    localRoleName = Column(String(50), nullable=False, server_default=text("''"))
    roleLevel = Column(String(1), nullable=False, server_default=text("''"))
    roleType = Column(String(1), nullable=False, server_default=text("''"))
    openDirectory = Column(String(1), nullable=False, server_default=text("''"))
    openPortal = Column(String(1), nullable=False, server_default=text("''"))
    ownerUid = Column(String(15))
    roleTermTo = Column(DateTime)
    warningMailFlag = Column(String(1))
    condition1Field = Column(String(50))
    condition1Operator = Column(String(10))
    condition1Value = Column(String(50))
    condition2Field = Column(String(50))
    condition2Operator = Column(String(10))
    condition2Value = Column(String(50))
    condition3Field = Column(String(50))
    condition3Operator = Column(String(10))
    condition3Value = Column(String(50))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLEINROLEMEMBER(Base):
    __tablename__ = 'ROLEINROLEMEMBER'

    roleId = Column(String(6), primary_key=True, nullable=False, server_default=text("''"))
    memberRoleID = Column(String(6), primary_key=True, nullable=False, server_default=text("''"))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLEINROLEMEMBERAPPLY(Base):
    __tablename__ = 'ROLEINROLEMEMBERAPPLY'

    applyRequestNumber = Column(BigInteger, primary_key=True, server_default=text("(0)"))
    applyType = Column(String(1), nullable=False, server_default=text("''"))
    applyStatus = Column(String(1), nullable=False, server_default=text("''"))
    applyUid = Column(String(15), nullable=False, server_default=text("''"))
    applyDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    applyMailFlag = Column(String(1), nullable=False, server_default=text("''"))
    approvalUid = Column(String(15), nullable=False, server_default=text("''"))
    approvalDate = Column(DateTime)
    approvalMailFlag = Column(String(1))
    deleteDate = Column(DateTime)
    roleId = Column(String(6), nullable=False, server_default=text("''"))
    memberRoleId = Column(String(6), nullable=False, server_default=text("''"))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLEMEMBER(Base):
    __tablename__ = 'ROLEMEMBER'

    roleId = Column(String(6), primary_key=True, nullable=False, server_default=text("''"))
    memberUserId = Column(String(15), primary_key=True, nullable=False, index=True, server_default=text("''"))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


class ROLEMEMBERAPPLY(Base):
    __tablename__ = 'ROLEMEMBERAPPLY'

    applyRequestNumber = Column(BigInteger, primary_key=True, server_default=text("(0)"))
    applyType = Column(String(1), nullable=False, server_default=text("''"))
    applyStatus = Column(String(1), nullable=False, server_default=text("''"))
    applyUid = Column(String(15), nullable=False, server_default=text("''"))
    applyDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    applyMailFlag = Column(String(1), nullable=False, server_default=text("''"))
    approvalUid = Column(String(15), nullable=False, server_default=text("''"))
    approvalDate = Column(DateTime)
    approvalMailFlag = Column(String(1))
    deleteDate = Column(DateTime)
    roleId = Column(String(6), nullable=False, server_default=text("''"))
    memberUserId = Column(String(15), nullable=False, server_default=text("''"))
    createDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    updateDate = Column(DateTime, nullable=False, server_default=text("getdate()"))
    directoryReflectStartDate = Column(DateTime)
    directoryReflectEndDate = Column(DateTime)
    directoryCreateDate = Column(DateTime)
    directoryUpdateDate = Column(DateTime)


t_VALLUSERS = Table(
    'VALLUSERS', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VALLUSERS2 = Table(
    'VALLUSERS2', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VALLUSERS2U = Table(
    'VALLUSERS2U', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_UpperSn', String(40)),
    Column('v_UpperGivenName', String(40)),
    Column('v_UpperMiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_UpperCompany', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_UpperGlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_UpperOu', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_UpperGlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_UpperTitle', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_UpperOfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VDELETEROLE = Table(
    'VDELETEROLE', metadata,
    Column('v_RoleId', String(6)),
    Column('v_RoleLevel', String(1)),
    Column('v_DeleteDate', NullType),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VDELETEROLEINROLEMEMBER1 = Table(
    'VDELETEROLEINROLEMEMBER1', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberRoleId', String(6)),
    Column('v_DeleteDate', NullType),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VDELETEROLEINROLEMEMBER2 = Table(
    'VDELETEROLEINROLEMEMBER2', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberRoleId', String(6)),
    Column('v_DeleteDate', NullType),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VDELETEROLEUSER = Table(
    'VDELETEROLEUSER', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberUserId', String(15)),
    Column('v_DeleteDate', NullType),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VDELETEUSERS = Table(
    'VDELETEUSERS', metadata,
    Column('v_Uid', String(15)),
    Column('v_DeleteDate', NullType),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VNMLUSERS2 = Table(
    'VNMLUSERS2', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VNMLUSERS2U = Table(
    'VNMLUSERS2U', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_UpperSn', String(40)),
    Column('v_UpperGivenName', String(40)),
    Column('v_UpperMiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_UpperCompany', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_UpperGlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_UpperOu', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_UpperGlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_UpperTitle', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_UpperOfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VOTHERUSERS = Table(
    'VOTHERUSERS', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VOTHERUSERS2 = Table(
    'VOTHERUSERS2', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VOTHERUSERS2U = Table(
    'VOTHERUSERS2U', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_UpperSn', String(40)),
    Column('v_UpperGivenName', String(40)),
    Column('v_UpperMiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_UpperCompany', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_UpperGlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_UpperOu', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_UpperGlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_UpperTitle', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_UpperOfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2))
)


t_VROLE = Table(
    'VROLE', metadata,
    Column('v_RoleId', String(6)),
    Column('v_RoleName', String(50)),
    Column('v_LocalRoleName', String(50)),
    Column('v_RoleLevel', String(1)),
    Column('v_RoleType', String(1)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VROLEINROLEMEMBER1 = Table(
    'VROLEINROLEMEMBER1', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberRoleId', String(6)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VROLEINROLEMEMBER2 = Table(
    'VROLEINROLEMEMBER2', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberRoleId', String(6)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VROLEUSER = Table(
    'VROLEUSER', metadata,
    Column('v_RoleId', String(6)),
    Column('v_MemberUserId', String(15)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VUSERS = Table(
    'VUSERS', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)


t_VUSERS2 = Table(
    'VUSERS2', metadata,
    Column('v_Uid', String(15)),
    Column('v_Locale', String(2)),
    Column('v_Sn', String(40)),
    Column('v_GivenName', String(40)),
    Column('v_MiddleName', String(40)),
    Column('v_LocalSn', NullType),
    Column('v_LocalGivenName', NullType),
    Column('v_LocalMiddleName', NullType),
    Column('v_JpYomiSn', String(40)),
    Column('v_JpYomiGivenName', String(40)),
    Column('v_Net23MailAddress', String(100)),
    Column('v_Mail', String(100)),
    Column('v_LocalMailAddress', String(100)),
    Column('v_Mobile', String(20)),
    Column('v_Pager', String(20)),
    Column('v_TelephoneNumber', String(20)),
    Column('v_TelephoneNumber2', String(20)),
    Column('v_TelephoneNumber3', String(20)),
    Column('v_ExtensionNumber', String(20)),
    Column('v_ExtensionNumber2', String(20)),
    Column('v_ExtensionNumber3', String(20)),
    Column('v_FacsimileTelephoneNumber', String(20)),
    Column('v_ExtensionFacsimileNumber', String(20)),
    Column('v_ContractorCode', String(10)),
    Column('v_ContractorCompany', String(100)),
    Column('v_ContractorLocalCompany', NullType),
    Column('v_TitleLevel', String(1)),
    Column('v_EmploymentType', String(1)),
    Column('v_Description', String(120)),
    Column('v_LocalDescription', NullType),
    Column('v_ManagerUid', String(15)),
    Column('v_L', String(3)),
    Column('v_C', String(2)),
    Column('v_CompanyCode', String(10)),
    Column('v_OldCompanyCode', String(6)),
    Column('v_Company', String(100)),
    Column('v_LocalCompany', NullType),
    Column('v_JpYomiCompany', String(160)),
    Column('v_CompanyDisc', String(4)),
    Column('v_ConnectiveType', String(1)),
    Column('v_CompanyPostalCode', NullType),
    Column('v_CompanyPostalAddress', String(120)),
    Column('v_CompanyLocalPostalAddress', NullType),
    Column('v_CompanyTelephoneNumber', String(20)),
    Column('v_GlobalCompanyCode', NullType),
    Column('v_LocalOuCode', String(6)),
    Column('v_Ou', NullType),
    Column('v_LocalOu', NullType),
    Column('v_LocalOperationDivisionCode', String(6)),
    Column('v_OperationDivisionName', String(255)),
    Column('v_LocalOperationDivisionName', NullType),
    Column('v_LocalDivisionCode', String(6)),
    Column('v_DivisionName', String(255)),
    Column('v_LocalDivisionName', NullType),
    Column('v_LocalDepartmentCode', String(6)),
    Column('v_DepartmentName', String(255)),
    Column('v_LocalDepartmentName', NullType),
    Column('v_LocalSectionCode', String(6)),
    Column('v_SectionName', String(255)),
    Column('v_LocalSectionName', NullType),
    Column('v_TeamCode', String(4)),
    Column('v_GlobalFunctionCode', NullType),
    Column('v_LocalTitleCode', String(2)),
    Column('v_Title', NullType),
    Column('v_LocalTitle', NullType),
    Column('v_OfficeCode', String(4)),
    Column('v_OfficeName', String(100)),
    Column('v_LocalOfficeName', NullType),
    Column('v_OfficePostalCode', NullType),
    Column('v_OfficePostalAddress', String(120)),
    Column('v_LocalOfficePostalAddress', NullType),
    Column('v_OfficeTelephoneNumber', String(20)),
    Column('v_GlobalBusinessCode', String(2)),
    Column('v_CreateDate', DateTime),
    Column('v_UpdateDate', DateTime),
    Column('v_DirectoryReflectStartDate', DateTime),
    Column('v_DirectoryReflectEndDate', DateTime)
)
