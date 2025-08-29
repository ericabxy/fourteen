<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<head>
  <style>
    dt {
      color: limegreen;
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
      <span style="float:right;" class="radius">
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
    <p class="description">
      <xsl:variable name="range" select="@range"/>
      <xsl:variable name="radius" select="@radius"/>
      <xsl:for-each select="primary-effect">
        <xsl:value-of select="current()"/><br/>
        <dl>
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
      </xsl:for-each>
      <xsl:for-each select="deliver-attack">
        Delivers
        <xsl:choose>
          <xsl:when test="$range &gt; 3">
            a ranged
          </xsl:when>
          <xsl:otherwise>
            an
          </xsl:otherwise>
        </xsl:choose>
        attack with a potency of <xsl:value-of select="@potency"/>
        <xsl:choose>
          <xsl:when test="$radius &gt; 0">
            <xsl:choose>
              <xsl:when test="$range &gt; 0">
                to target and all enemies nearby it.
              </xsl:when>
              <xsl:otherwise>
                to all nearby enemies.
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:otherwise>.</xsl:otherwise>
        </xsl:choose>
      </xsl:for-each><!-- for each attack -->
      <xsl:for-each select="deal-damage">
        Deals
        <xsl:value-of select="@aspect"/>
        damage with a potency of <xsl:value-of select="@potency"/>
        <xsl:choose>
          <xsl:when test="$radius &gt; 0">
            <xsl:choose>
              <xsl:when test="$range &gt; 0">
                to target and all enemies nearby it.
              </xsl:when>
              <xsl:otherwise>
                <xsl:choose>
                  <xsl:when test="@area = 'circle'">
                    to all nearby enemies.
                  </xsl:when>
                  <xsl:when test="@area = 'line'">
                    to all enemies in a straight line before you.
                  </xsl:when>
                  <xsl:when test="@area = 'cone'">
                    to all enemies in a cone before you.
                  </xsl:when>
                </xsl:choose>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:otherwise>.</xsl:otherwise>
        </xsl:choose>
      </xsl:for-each><!-- for each damage -->
      <xsl:for-each select="increase">
        Increases
        <xsl:value-of select="current()"/>
          by
        <xsl:value-of select="@percent"/>%.
        <dl>
          <dt>Duration</dt>
          <dd><xsl:value-of select="@duration div 1000"/>s</dd>
        </dl>
      </xsl:for-each>
      <xsl:for-each select="reduce">
        Reduces
        <xsl:value-of select="current()"/>
        by
        <xsl:value-of select="@percent"/>%.
        <dl>
          <dt>Duration</dt>
          <dd><xsl:value-of select="@duration div 1000"/>s</dd>
        </dl>
      </xsl:for-each>
    </p><!-- description -->
    <xsl:for-each select="./combination">
      <dl>
      <xsl:for-each select="./combo-action">
          <dt>Combo Action</dt>
          <dd style="color:orange;"><xsl:value-of select="current()"/></dd>
          <dt>Combo Potency</dt>
          <dd><xsl:value-of select="./@potency"/></dd>
      </xsl:for-each>
      <xsl:for-each select="./combo-bonus">
          <dt>Combo Bonus</dt>
            <xsl:choose>
              <xsl:when test="grant">
                <dd>
                  Grants
                  <span style="color:yellow;">
                    <xsl:value-of select="grant"/>
                  </span>
                </dd>
              </xsl:when>
              <xsl:otherwise>
                <dd><xsl:value-of select="current()"/></dd>
              </xsl:otherwise>
            </xsl:choose>
          <xsl:if test="@cure">
            <dt>Cure Potency</dt>
            <dd><xsl:value-of select="@cure"/></dd>
          </xsl:if>
          <xsl:if test="@duration">
            <dt>Duration</dt>
            <dd><xsl:value-of select="@duration div 1000"/>s</dd>
          </xsl:if>
      </xsl:for-each>
      </dl>
    </xsl:for-each>
    <xsl:for-each select="./additional-effect">
      <dl>
        <dt>Additional Effect</dt>
        <xsl:choose>
          <xsl:when test="grant">
            <dd>
              Grants
              <span style="color:yellow;">
                <xsl:value-of select="grant"/>
              </span>
            </dd>
          </xsl:when>
          <xsl:otherwise>
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
    </xsl:for-each>
    <xsl:for-each select="./granted-effect">
      <dl>
        <dt><xsl:value-of select="./name"/> Effect</dt>
        <dd><xsl:value-of select="./description"/></dd>
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
    </xsl:for-each>
    <xsl:for-each select="./job-gauge">
      <dl>
        <dt><xsl:value-of select="current()"/> Cost</dt>
        <dd><xsl:value-of select="@cost"/></dd>
      </dl>
    </xsl:for-each>
    <xsl:for-each select="./extend-duration">
      <div>
        Extends
        <span style="color:yellow;">
          <xsl:value-of select="current()"/>
        </span>
        duration by
        <xsl:value-of select="@extend div 1000"/>s
        to a maximum of
        <xsl:value-of select="@maximum div 1000"/>s.
      </div>
    </xsl:for-each>
    <xsl:for-each select="./share-recast">
      <div>
        <xsl:value-of select="current()"/>
      </div>
    </xsl:for-each>
    <xsl:if test="./bullet-point">
      <ul>
      <xsl:for-each select="./bullet-point">
          <li><xsl:value-of select="current()"/></li>
      </xsl:for-each>
      </ul>
    </xsl:if>
  </div>
</xsl:for-each>
</body>
</html>
