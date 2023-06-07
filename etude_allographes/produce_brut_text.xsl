<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0"
    xmlns:tei="http://www.tei-c.org/ns/1.0">
    
    <xsl:output method="text"/>
    <xsl:strip-space elements="*"/>
    
    <xsl:template match="tei:g">
        <xsl:variable name="id" select="translate(@ref, '#', '')"/>
        <xsl:value-of select="//tei:char[@xml:id = $id]/descendant-or-self::tei:mapping[1]"/>
    </xsl:template>
    
    
    <xsl:template match="tei:fw | tei:expan | tei:reg | tei:teiHeader | tei:note"/>
    
    <xsl:template match="tei:lb">
        <xsl:choose>
            <xsl:when test="@break = 'yes'">
                <xsl:text>_||&#10;</xsl:text>
            </xsl:when>
            <xsl:otherwise>-||&#10;</xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
