<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">



    <xsl:template match="@* | node()">
        <xsl:copy copy-namespaces="yes">
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>


    <xsl:template
        match="tei:teiHeader | tei:facsimile | tei:div[@n = '2'][@type = 'partie'] | tei:div[@type = 'seuil']"/>


    <xsl:template match="/">
        <xsl:result-document href="corpora/complet/corpus_complet.xml">
            <xsl:apply-templates/>
        </xsl:result-document>
    </xsl:template>

    <xsl:template match="tei:text">
        <xsl:element name="text" namespace="http://www.tei-c.org/ns/1.0">
            <xsl:attribute name="xml:id" select="parent::tei:TEI/@xml:id"/>
            <xsl:attribute name="n" select="parent::tei:TEI/@xml:id"/>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>



</xsl:stylesheet>
