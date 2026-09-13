import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function BentoNativeOverview({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.grid, compact && styles.compact]}>
      <View style={styles.tile}>
        <Text style={styles.title}>Overview</Text>
        <Text style={styles.body}>Keep the DOM/content order meaningful when the grid collapses.</Text>
        <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
          <Text style={styles.label}>View</Text>
        </Pressable>
      </View>
      <View style={styles.tileSecondary}><Text style={styles.body}>Secondary content</Text></View>
    </View>
  );
}

const styles = StyleSheet.create({
  grid: { flexDirection: 'row', gap: 12, padding: 20 },
  compact: { flexDirection: 'column', padding: 16 },
  tile: { flex: 2, minHeight: 180, padding: 20, borderRadius: 18, borderWidth: 1, borderColor: '#a0a6af', backgroundColor: '#f7f8fa' },
  tileSecondary: { flex: 1, minHeight: 180, padding: 20, borderRadius: 18, borderWidth: 1, borderColor: '#c0c4ca', backgroundColor: '#eceff4' },
  title: { fontSize: 20, fontWeight: '800' },
  body: { marginTop: 8, color: '#2e333a' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 14, backgroundColor: '#e5ebff' },
  pressed: { opacity: 0.78 },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: content-first row/column adaptation, meaningful order, native interaction, explicit state.
// Fallback: collapse tiles vertically without changing content priority.
