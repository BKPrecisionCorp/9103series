<?xml version='1.0' encoding='UTF-8'?>
<Project Name="Template - DC Power.lvproj" Type="Project" LVVersion="19008000" URL="/&lt;instrlib&gt;/_Template - DC Power/Template - DC Power.lvproj">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Project.Description" Type="Str">This project is used by developers to edit API and example files for LabVIEW Plug and Play instrument drivers.</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="CCSymbols" Type="Str">OS,Win;CPU,x86;</Property>
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Examples" Type="Folder"/>
		<Item Name="9103Series.lvlib" Type="Library" URL="/&lt;instrlib&gt;/9103Series/9103Series.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
			</Item>
			<Item Name="instr.lib" Type="Folder">
				<Item Name="Error Query.vi" Type="VI" URL="/&lt;instrlib&gt;/9103Series/Public/Utility/Error Query.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
