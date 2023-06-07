<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">


    <xsl:variable name="array" as="element()*">
        <Item>Mad_A</Item>
        <Item>Mad_B</Item>
        <Item>Mad_G</Item>
        <Item>Sal_J</Item>
        <Item>Esc_Q</Item>
        <Item>Sev_R</Item>
        <Item>Phil_U</Item>
        <Item>Sev_Z</Item>
    </xsl:variable>

    <xsl:template match="tei:app[contains(@ana, 'lexicale')]">
        <xsl:for-each select="$array">
            <xsl:if test="descendant::tei:rdg[contains(@wit, .)]">
                
            </xsl:if>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="tei:rdgGrp"> </xsl:template>


</xsl:stylesheet>
