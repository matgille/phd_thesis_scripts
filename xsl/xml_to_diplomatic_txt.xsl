<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs" version="2.0">


    <xsl:output method="text"/>



    <xsl:template match="/">
        <xsl:for-each
            select="collection('/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/analyse_linguistique?select=*.xml')/tei:TEI">
            <xsl:message select="@xml:id"/>
            <xsl:result-document href="datasets/{@xml:id}.txt">
                <xsl:apply-templates/>
            </xsl:result-document>
            <xsl:message>Travail terminé.</xsl:message>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="tei:teiHeader | tei:note | tei:add[@type = 'commentaire']"/>


    <xsl:template match="text()">
        <xsl:variable name="var1" select="replace(., '\n', '')"/>
        <xsl:value-of select="replace($var1, '\s{2,20}', ' ')"/>
    </xsl:template>


    <xsl:template match="tei:w">
        <xsl:text> </xsl:text>
        <xsl:apply-templates/>
        <xsl:text> </xsl:text>
    </xsl:template>

    <xsl:template match="tei:lb[@break = 'yes']">
        <xsl:text>
        </xsl:text>
    </xsl:template>



    <xsl:template match="tei:lb[@break = 'no']"/>


    <xsl:template match="tei:pc">
        <xsl:apply-templates/>
        <xsl:text> </xsl:text>
    </xsl:template>


    <xsl:template match="tei:choice">
        <xsl:apply-templates select="tei:orig | tei:abbr"/>
    </xsl:template>

    <!--
    <xsl:template match="tei:div[@type = 'chapitre']">
        <xsl:text>&#10;&#10;&#10; Chapitre</xsl:text>
        <xsl:value-of select="@n"/>
        <xsl:text>&#10;&#10;</xsl:text>
        <xsl:apply-templates/>
    </xsl:template>-->



    <xsl:template match="tei:fw"/>

    <xsl:template match="tei:head"/>

    <xsl:template match="tei:abbr">
        <xsl:choose>
            <xsl:when test="tei:g">
                <xsl:variable name="ref" select="translate(descendant::*:g/@ref, '#', '')"/>
                <xsl:value-of select="//*:char[@xml:id = $ref]/*:mapping[1]"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="."/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="tei:g">
        <xsl:variable name="ref" select="translate(@ref, '#', '')"/>
        <xsl:value-of select="//*:char[@xml:id = $ref]/*:mapping[1]"/>
    </xsl:template>

    <xsl:template match="tei:orig">
        <xsl:choose>
            <xsl:when test="tei:g">
                <xsl:apply-templates select="tei:g"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="."/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>


    <xsl:template match="tei:space">
        <xsl:text> </xsl:text>
    </xsl:template>






</xsl:stylesheet>
