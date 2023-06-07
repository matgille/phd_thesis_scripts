<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs" version="2.0">

    <xsl:output method="text"/>


    <xsl:template match="/">
        <xsl:result-document href="output.txt">
            <xsl:for-each
                select="descendant::tei:TEI[@xml:id = 'Sal_J']//tei:div[@type = 'chapitre']">
                <xsl:variable name="n" select="@n"/>
                <xsl:text>Chapitre </xsl:text>
                <xsl:value-of select="$n"/>
                <xsl:text> --  Nombre de notes générales: </xsl:text>
                <xsl:value-of
                    select="count(//tei:div[@type = 'chapitre'][@n = $n]//tei:note[@type = 'general']) + count(//tei:div[@type = 'chapitre'][@n = $n]//tei:note[@subtype = 'variante'])"/>
                <xsl:text> --  Nombre de milestones: </xsl:text>
                <xsl:value-of
                    select="count(//tei:TEI[@xml:id = 'Sev_Z']//tei:div[@type = 'chapitre'][@n = $n]//tei:milestone[@unit])"/>
                <xsl:apply-templates/>

            </xsl:for-each>
        </xsl:result-document>
    </xsl:template>


    <xsl:template match="tei:div[@type = 'glose']">
        <xsl:text>Glose</xsl:text>
        <xsl:apply-templates/>
    </xsl:template>
    
    
    
    <xsl:template match="tei:div[@type = 'traduction']">
        <xsl:text>Traduction</xsl:text>
        <xsl:apply-templates/>
    </xsl:template>
    <!--Ajouter une fonction qui vérifie que tous les chapitres ont bien le même 
        nombre de paragraphes que J (i.e., qu'il n'y ait pas une modification qui n'ait pas été portée sur j)-->

    <xsl:template match="tei:head | tei:note"/>
    <xsl:template match="tei:p[@n]">
        <xsl:variable name="n" select="@n"/>
        <xsl:value-of select="$n"/>
        <xsl:text>: </xsl:text>
        <xsl:for-each select="ancestor::tei:TEI//tei:TEI[@type = 'transcription']">
            <xsl:if test="not(descendant::tei:p[@n = $n])">
                <xsl:text>Error in </xsl:text>
                <xsl:value-of select="@xml:id"/>
                <xsl:text> </xsl:text>
            </xsl:if>
        </xsl:for-each>
    </xsl:template>


</xsl:stylesheet>
