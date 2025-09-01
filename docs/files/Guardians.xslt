<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<head>
  <title>Character</title>
  <style>
    dt {
      color: limegreen;
    }
    dd img, dd span {
      vertical-align: middle;
    }
    dl.acquired dt {
      color: cornsilk;
    }
  </style>
</head>
<body>
<xsl:for-each select="character/*">
  <div style="background-color:dimgray; border:5px outset gray; color:white; margin:1em; padding:1em;">
    <h3><xsl:value-of select="name"/></h3>
    <div class="statblock">
      <span style="text-transform:capitalize;">
        <xsl:value-of select="name()"/>
      </span>
      <span style="float:right;" class="range">
        Range
        <xsl:choose>
          <xsl:when test="@range">
            <xsl:value-of select="@range"/>m
          </xsl:when>
          <xsl:otherwise>
            0m
          </xsl:otherwise>
        </xsl:choose>
      </span>
      <span style="float:right; padding-right:1em;" class="radius">
        Radius
        <xsl:choose>
          <xsl:when test="@radius">
            <xsl:value-of select="@radius"/>m
          </xsl:when>
          <xsl:otherwise>
            0m
          </xsl:otherwise>
        </xsl:choose>
      </span>
    </div>
    <table>
      <tr>
        <td style="text-align:right;">Cast</td>
        <td style="text-align:right;">Recast</td>
        <xsl:if test="@mpcost">
          <td style="text-align:right;">MP Cost</td>
        </xsl:if>
      </tr>
      <tr>
        <td style="border-bottom:8px solid darkgray; text-align:right;">
          <xsl:choose>
            <xsl:when test="cast &gt; 0">
              <xsl:value-of select="@cast"/>
            </xsl:when>
            <xsl:otherwise>
              Instant
            </xsl:otherwise>
          </xsl:choose>
        </td>
        <td style="border-bottom:8px solid darkgray; text-align:right;">
          <xsl:value-of select="@recast div 1000"/>s
        </td>
        <td style="border-bottom:8px solid darkgray; text-align:right;">
          <xsl:value-of select="@mpcost"/>
        </td>
      </tr>
    </table>
    <hr/>
    <div class="description">
      <xsl:for-each select="*">
        <xsl:if test="name(.) = 'additional-effect'">
          <dl>
            <xsl:choose>
              <xsl:when test="name">
                <dt><xsl:value-of select="name"/> Effect</dt>
                <dd><xsl:value-of select="description"/></dd>
              </xsl:when>
              <xsl:otherwise>
                <dt>Additional Effect</dt>
                <dd><xsl:value-of select="current()"/></dd>
              </xsl:otherwise>
            </xsl:choose>
            <xsl:if test="@potency">
              <dt>Potency</dt>
              <dd><xsl:value-of select="@potency"/></dd>
            </xsl:if>
            <xsl:if test="@duration">
              <dt>Duration</dt>
              <dd><xsl:value-of select="@duration div 1000"/>s</dd>
            </xsl:if>
            <xsl:if test="@cure-potency">
              <dt>Cure Potency</dt>
              <dd><xsl:value-of select="@cure-potency"/></dd>
            </xsl:if>
          </dl>
        </xsl:if>
        <xsl:if test="name(.) = 'combo-action'">
          <dl>
            <dt>Combo Action</dt>
            <dd style="color:orange;"><xsl:value-of select="current()"/></dd>
            <dt>Combo Potency</dt>
            <dd><xsl:value-of select="./@potency"/></dd>
          </dl>
        </xsl:if>
        <xsl:if test="name(.) = 'combo-bonus'">
          <dl>
            <dt>Combo Bonus</dt>
            <dd><xsl:value-of select="current()"/></dd>
            <xsl:if test="@cure-potency">
              <dt>Cure Potency</dt>
              <dd><xsl:value-of select="@cure-potency"/></dd>
            </xsl:if>
            <xsl:if test="@duration">
              <dt>Duration</dt>
              <dd><xsl:value-of select="@duration div 1000"/>s</dd>
            </xsl:if>
          </dl>
        </xsl:if>
        <!--Extend Duration-->
        <xsl:if test="name(.) = 'extend-duration'">
          <div>
            Extends
            <span style="color:yellow;">
              <xsl:value-of select="current()"/>
            </span>
            duration by
            <span style="color:black;"><xsl:value-of select="@extend div 1000"/>s</span>
            to a maximum of
            <xsl:value-of select="@maximum div 1000"/>s.
          </div>
        </xsl:if>
        <!--Limitation-->
        <xsl:if test="name(.) = 'limitation'">
          <p>
            <xsl:value-of select="current()"/>
          </p>
        </xsl:if>
        <xsl:if test="name(.) = 'named-potency'">
          <dl>
            <dt><xsl:value-of select="current()"/> Potency</dt>
            <dd><xsl:value-of select="@potency"/></dd>
          </dl>
        </xsl:if>
        <xsl:if test="name(.) = 'named-cost'">
          <dl>
            <dt><xsl:value-of select="current()"/> Cost</dt>
            <dd><xsl:value-of select="@cost"/></dd>
          </dl>
        </xsl:if>
        <!--Primary Effect-->
        <xsl:if test="name(.) = 'primary-effect'">
          <p>
            <xsl:value-of select="current()"/>
          </p>
          <xsl:if test="@area or @attack or @damage or @potency or @target">
            <p>
              <xsl:if test="@area">
                <span style="color:SkyBlue">Area:</span>
                <xsl:value-of select="@area"/>
              </xsl:if>
              <xsl:if test="@attack">
                <span style="color:SkyBlue">Attack Type:</span>
                <xsl:value-of select="@attack"/>
              </xsl:if>
              <xsl:if test="@damage">
                <span style="color:SkyBlue">Damage Aspect:</span>
                <xsl:value-of select="@damage"/>
              </xsl:if>
              <xsl:if test="@potency">
                <span style="color:SkyBlue">Potency:</span>
                <xsl:value-of select="@potency"/>
              </xsl:if>
              <xsl:if test="@target">
                <span style="color:SkyBlue">Target:</span>
                <xsl:value-of select="@target"/>
              </xsl:if>
            </p>
          </xsl:if>
          <dl>
            <xsl:if test="@duration">
              <dt>Duration</dt>
              <dd><xsl:value-of select="@duration div 1000"/>s</dd>
            </xsl:if>
            <xsl:if test="@cure-potency">
              <dt>Cure Potency</dt>
              <dd><xsl:value-of select="@cure-potency"/></dd>
            </xsl:if>
            <xsl:if test="@maximum-charges">
              <dt>Maximum Charges</dt>
              <dd><xsl:value-of select="@maximum-charges"/></dd>
            </xsl:if>
          </dl>
        </xsl:if>
        <xsl:if test="name(.) = 'share-recast'">
          <div>
            <xsl:value-of select="current()"/>
          </div>
        </xsl:if>
      </xsl:for-each>
    </div><!-- description -->
    <xsl:if test="./bullet-point">
      <ul>
      <xsl:for-each select="./bullet-point">
          <li><xsl:value-of select="current()"/></li>
      </xsl:for-each>
      </ul>
    </xsl:if>
    <dl class="acquired">
      <dt>Acquired</dt>
      <dd>
        <img src="files/Fighter.png"/>
        <span>
          Lv. <xsl:value-of select="@level"/>
        </span>
      </dd>
    </dl>
  </div>
</xsl:for-each>
</body>
</html>
