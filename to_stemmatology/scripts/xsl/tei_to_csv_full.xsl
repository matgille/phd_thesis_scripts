<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs"
    xmlns:xi="http://www.w3.org/2001/XInclude" version="2.0">
    <!--Cette feuille permet de produire un document csv qui sera utilisé pour filtrer les variantes lexicales.-->
    <xsl:output method="text"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">
        <xsl:result-document href="../data/a_filtrer_full.csv">
            <xsl:for-each select="$tokens">
                <xsl:value-of select="."/>
                <xsl:text>,</xsl:text>
            </xsl:for-each>
            <xsl:text>Analyse, Chapitre, Type, Conserver, Revoir</xsl:text>
            <xsl:text>&#10;</xsl:text>
            <xsl:apply-templates select="//tei:app"/>
        </xsl:result-document>
    </xsl:template>
    <xsl:variable name="tokens" select="tokenize('A B G J Q R Z U', '\s')"/>


    <xsl:template match="tei:note | tei:desc"/>
    <xsl:template match="tei:hi"/>

    <xsl:template match="tei:choice">
        <xsl:apply-templates select="tei:reg | tei:corr"/>
    </xsl:template>


    <xsl:template match="tei:app">
        <xsl:variable name="position" select="position()"/>
        <xsl:variable name="self" select="self::node()"/>
        <xsl:value-of select="$position"/>
        <xsl:text>,</xsl:text>
        <xsl:for-each select="$tokens">
            <xsl:variable name="current_sigla">
                <xsl:value-of select="."/>
            </xsl:variable>
            <xsl:choose>
                <xsl:when test="$self/descendant::tei:rdg[contains(@wit, $current_sigla)]/tei:w">
                    <xsl:variable name="var">
                        <xsl:apply-templates
                            select="$self/descendant::tei:rdg[contains(@wit, $current_sigla)]/tei:w"/>
                    </xsl:variable>
                    <xsl:value-of select="replace($var, '\s+', '')"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>ø</xsl:text>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text>,</xsl:text>
        </xsl:for-each>
        <xsl:value-of select="@ana"/>
        <xsl:text>,</xsl:text>
        <xsl:value-of select="ancestor::tei:div[@type = 'chapitre']/@n"/>
        <xsl:text>,</xsl:text>
        <xsl:value-of select="ancestor::tei:div[@type = 'glose' or @type = 'traduction']/@type"/>
        <xsl:text>,</xsl:text>
        <xsl:text>Non, Non</xsl:text>
        <xsl:text>&#10;</xsl:text>
    </xsl:template>



</xsl:stylesheet>
