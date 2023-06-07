<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">


    <xsl:template match="@* | node()" mode="remove_traduction">
        <xsl:choose>
            <xsl:when test="ancestor-or-self::tei:div[@type = 'glose']">
                <xsl:copy copy-namespaces="yes">
                    <xsl:apply-templates select="@* | node()"/>
                </xsl:copy>
            </xsl:when>
            <xsl:otherwise/>
        </xsl:choose>
    </xsl:template>


    <xsl:template match="@* | node()" mode="remove_glose">
        <xsl:choose>
            <xsl:when test="ancestor-or-self::tei:div[@type = 'traduction']">
                <xsl:copy copy-namespaces="yes">
                    <xsl:apply-templates select="@* | node()"/>
                </xsl:copy>
            </xsl:when>
            <xsl:otherwise/>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="@* | node()" mode="remove_glose">
        <xsl:copy copy-namespaces="yes">
            <xsl:apply-templates select="@* | node()" mode="remove_glose"/>
        </xsl:copy>
    </xsl:template>


    <xsl:template match="tei:teiHeader | tei:facsimile" mode="#all"/>


    <xsl:template match="/">
        <xsl:result-document href="corpus_traduction.xml">
            <xsl:apply-templates mode="remove_glose"/>
        </xsl:result-document>
        <xsl:result-document href="corpus_glose.xml">
            <xsl:apply-templates mode="remove_translation"/>
        </xsl:result-document>
    </xsl:template>


    <xsl:template match="tei:div[@type = 'glose']" mode="remove_glose"/>
    <xsl:template match="tei:div[@type = 'traduction']" mode="remove_translation"/>

</xsl:stylesheet>
