import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function ClaymorphismNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.card, compact && styles.compact]}>
      <Text style={styles.title}>Soft volume</Text>
      <Text style={styles.body}>Keep the inflated surface expressive, but make interaction state explicit.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>Start</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderRadius: 28, backgroundColor: '#cfd4ff', shadowColor: '#51445b', shadowOpacity: 0.25, shadowRadius: 12, shadowOffset: { width: 0, height: 8 }, elevation: 7 },
  compact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#292737' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 18, justifyContent: 'center', borderRadius: 16, backgroundColor: '#eceeff', shadowColor: '#4b4160', shadowOpacity: 0.16, shadowRadius: 5, shadowOffset: { width: 0, height: 3 } },
  pressed: { transform: [{ translateY: 1 }], shadowOpacity: 0.05 },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: native semantics, bounded volume effects, compact layout, pressed/disabled state.
// Fallback: flatten shadow/highlight while retaining opaque surfaces and boundaries.
