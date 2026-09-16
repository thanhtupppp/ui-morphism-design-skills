import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function BentoNativeOverview({
  onOpenDashboard,
  onReviewAlerts,
}: {
  onOpenDashboard?: () => void;
  onReviewAlerts?: () => void;
}) {
  const width = useWindowDimensions().width;
  const compact = width < 768;
  const medium = width >= 768 && width < 1024;

  return (
    <View style={[styles.grid, compact && styles.compactGrid, medium && styles.mediumGrid]}>
      <View style={[styles.tile, styles.heroTile]}>
        <Text style={styles.eyebrow}>Overview</Text>
        <Text accessibilityRole="header" style={styles.title}>Operations</Text>
        <Text style={styles.body}>Primary task and key metric receive the largest area.</Text>
        <Pressable
          accessibilityRole="button"
          accessibilityState={{ disabled: !onOpenDashboard }}
          disabled={!onOpenDashboard}
          onPress={onOpenDashboard}
          style={({ pressed }) => [styles.button, pressed && styles.pressed, !onOpenDashboard && styles.disabled]}
        >
          <Text style={styles.label}>Open dashboard</Text>
        </Pressable>
      </View>

      <View style={[styles.tile, styles.wideTile]}>
        <Text style={styles.eyebrow}>Today</Text>
        <Text accessibilityRole="header" style={styles.subtitle}>Energy usage</Text>
        <Text style={styles.metric}>24.8 kWh</Text>
      </View>

      <View style={[styles.tile, styles.supportingTile]}>
        <Text style={styles.eyebrow}>Status</Text>
        <Text accessibilityRole="header" style={styles.subtitle}>Alerts</Text>
        <Text style={styles.metric}>3 open</Text>
        <Pressable
          accessibilityRole="button"
          accessibilityState={{ disabled: !onReviewAlerts }}
          disabled={!onReviewAlerts}
          onPress={onReviewAlerts}
          style={({ pressed }) => [styles.button, pressed && styles.pressed, !onReviewAlerts && styles.disabled]}
        >
          <Text style={styles.label}>Review alerts</Text>
        </Pressable>
      </View>

      <View style={[styles.tile, styles.utilityTile]}>
        <Text style={styles.eyebrow}>Service</Text>
        <Text accessibilityRole="header" style={styles.subtitle}>Uptime</Text>
        <Text style={styles.metric}>99.9%</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 16, padding: 24, backgroundColor: '#f7f8fa' },
  compactGrid: { flexDirection: 'column', padding: 16 },
  mediumGrid: { padding: 20 },
  tile: { minWidth: 0, padding: 20, borderRadius: 24, borderWidth: 1, borderColor: '#e2e8f0', backgroundColor: '#fff' },
  heroTile: { flexBasis: '48%', flexGrow: 2 },
  wideTile: { flexBasis: '48%', flexGrow: 1 },
  supportingTile: { flexBasis: '31%', flexGrow: 1 },
  utilityTile: { flexBasis: '23%', flexGrow: 1 },
  eyebrow: { color: '#64748b', fontSize: 13, fontWeight: '700' },
  title: { marginTop: 4, fontSize: 24, fontWeight: '800', color: '#18202a' },
  subtitle: { marginTop: 4, fontSize: 20, fontWeight: '800', color: '#18202a' },
  body: { marginTop: 8, color: '#475569' },
  metric: { marginTop: 8, fontSize: 18, fontWeight: '700', color: '#18202a' },
  button: { marginTop: 16, minWidth: 48, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 12, borderWidth: 1, borderColor: '#cbd5e1', backgroundColor: '#fff' },
  pressed: { opacity: 0.78 },
  disabled: { opacity: 0.55 },
  label: { textAlign: 'center', fontWeight: '700', color: '#18202a' },
});

// Verification: source order stays Operations → Energy usage → Alerts → Uptime across responsive reflow.
// Fallback: stack every tile vertically without changing semantic priority or interaction state.
